import streamlit as st
import plotly.graph_objects as go
import numpy as np
from streamlit_plotly_events import plotly_events

# ----------------------------------------
# Retrieve grid dimensions from session or fallback
# ----------------------------------------
Nx = st.session_state.get("Nx", 10)
Ny = st.session_state.get("Ny", 10)
dx = st.session_state.get("dx", 100.0)
dy = st.session_state.get("dy", 100.0)

# ----------------------------------------
# Initialize session state for wells
# ----------------------------------------
if "wells" not in st.session_state:
    st.session_state.wells = []
if "P_counter" not in st.session_state:
    st.session_state.P_counter = 1
if "I_counter" not in st.session_state:
    st.session_state.I_counter = 1

# ----------------------------------------
# Helper to add a new well
# ----------------------------------------
def add_well(well_type, i, j, rate):
    if well_type == "Producer":
        name = f"P_{st.session_state.P_counter}"
        st.session_state.P_counter += 1
        color = "black"
    else:
        name = f"I_{st.session_state.I_counter}"
        st.session_state.I_counter += 1
        color = "blue"

    st.session_state.wells.append({
        "name": name,
        "type": well_type.lower(),
        "i": i,
        "j": j,
        "rate": rate,
        "color": color
    })

# ----------------------------------------
# Layout - Well Input (Manual Placement)
# ----------------------------------------
st.subheader("🛢️ Manual Well Placement")
with st.form("manual_well_form"):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        well_type = st.selectbox("Well Type", ["Producer", "Injector"], key="manual_type")
    with col2:
        i = st.number_input("Grid i (x)", min_value=0, max_value=Nx - 1, value=0, key="manual_i")
    with col3:
        j = st.number_input("Grid j (y)", min_value=0, max_value=Ny - 1, value=0, key="manual_j")
    with col4:
        rate = st.number_input("Rate (STB/day)", min_value=0.0, value=500.0, key="manual_rate")
    submitted = st.form_submit_button("➕ Add Well")
    if submitted:
        add_well(well_type, int(i), int(j), rate)
        st.success(f"{well_type} well added at ({i}, {j})")

# ----------------------------------------
# Delete Wells
# ----------------------------------------
st.subheader("🗑️ Remove a Well")
well_names = [w["name"] for w in st.session_state.wells]
if well_names:
    well_to_remove = st.selectbox("Select Well to Remove", well_names)
    if st.button("❌ Delete Selected Well"):
        st.session_state.wells = [w for w in st.session_state.wells if w["name"] != well_to_remove]
        st.success(f"Deleted well {well_to_remove}")
else:
    st.info("No wells added yet.")

# ----------------------------------------
# Grid Plotting with Plotly (Hover & Click)
# ----------------------------------------
st.subheader("📍 2D Grid Map with Wells (Click-to-Add)")
x_vals = np.arange(0, Nx * dx + dx, dx)
y_vals = np.arange(0, Ny * dy + dy, dy)

fig = go.Figure()
for x in x_vals:
    fig.add_shape(type="line", x0=x, y0=0, x1=x, y1=Ny * dy, line=dict(color="lightgray", width=1))
for y in y_vals:
    fig.add_shape(type="line", x0=0, y0=y, x1=Nx * dx, y1=y, line=dict(color="lightgray", width=1))

# Add wells to plot
for well in st.session_state.wells:
    x = well["i"] * dx + dx / 2
    y = well["j"] * dy + dy / 2
    fig.add_trace(go.Scatter(x=[x], y=[y], mode='markers+text',
                             marker=dict(color=well["color"], size=12),
                             text=[well["name"]],
                             textposition="top center"))

fig.update_layout(
    title="Reservoir Grid View",
    xaxis=dict(title="x (ft)", range=[0, Nx * dx], tick0=0, dtick=dx, showgrid=False),
    yaxis=dict(title="y (ft)", range=[0, Ny * dy], tick0=0, dtick=dy, showgrid=False),
    height=600,
    width=800,
    clickmode='event+select'
)

click_result = plotly_events(fig, click_event=True, select_event=False, hover_event=False, key="click")

if click_result:
    clicked_x = click_result[0]['x']
    clicked_y = click_result[0]['y']
    grid_i = int(clicked_x // dx)
    grid_j = int(clicked_y // dy)
    st.info(f"You clicked at grid block ({grid_i}, {grid_j})")
    with st.form("click_add_form"):
        colA, colB = st.columns([2, 3])
        with colA:
            well_type = st.selectbox("Well Type", ["Producer", "Injector"], key="click_type")
        with colB:
            rate = st.number_input("Rate (STB/day)", min_value=0.0, value=500.0, key="click_rate")
        confirm = st.form_submit_button("✅ Confirm Placement")
        if confirm:
            add_well(well_type, grid_i, grid_j, rate)
            st.success(f"{well_type} well added at ({grid_i}, {grid_j})")

# ----------------------------------------
# Display Current Wells Table
# ----------------------------------------
st.markdown("### 💾 Current Wells")
if st.session_state.wells:
    st.dataframe(st.session_state.wells)
else:
    st.info("No wells added yet.")
