import streamlit as st
import plotly.graph_objects as go
import numpy as np

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

# ----------------------------------------
# Helper to get the next available index
# ----------------------------------------
def get_next_well_number(well_type):
    prefix = "P_" if well_type == "Producer" else "I_"
    existing_numbers = [int(w["name"].split("_")[1]) for w in st.session_state.wells if w["name"].startswith(prefix)]
    n = 1
    while n in existing_numbers:
        n += 1
    return n

# ----------------------------------------
# Helper to add a new well
# ----------------------------------------
def add_well(well_type, i, j, rate):
    number = get_next_well_number(well_type)
    if well_type == "Producer":
        name = f"P_{number}"
        color = "black"
    else:
        name = f"I_{number}"
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
# Grid Plotting with Plotly
# ----------------------------------------
st.subheader("📍 2D Grid Map with Wells")
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
                             textposition="top center",
                             showlegend=False))

fig.update_layout(
    title="Reservoir Grid View",
    xaxis=dict(title="i", range=[0, Nx * dx], tick0=0, dtick=dx, showgrid=False),
    yaxis=dict(title="j", range=[0, Ny * dy], tick0=0, dtick=dy, showgrid=False),
    height=600,
    width=800
)

st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------
# Display Current Wells Table
# ----------------------------------------
st.markdown("### 💾 Current Wells")
if st.session_state.wells:
    st.dataframe(st.session_state.wells)
else:
    st.info("No wells added yet.")
