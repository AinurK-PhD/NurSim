import streamlit as st
import matplotlib.pyplot as plt
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
        well_type = st.selectbox("Well Type", ["Producer", "Injector"])
    with col2:
        i = st.number_input("Grid i (x)", min_value=0, max_value=Nx - 1, value=0)
    with col3:
        j = st.number_input("Grid j (y)", min_value=0, max_value=Ny - 1, value=0)
    with col4:
        rate = st.number_input("Rate (STB/day)", min_value=0.0, value=500.0)
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
# Grid Plotting with Wells
# ----------------------------------------
st.subheader("📍 2D Grid Map with Wells")
fig, ax = plt.subplots(figsize=(8, 8 * Ny / Nx))

# Draw grid lines
for x in range(Nx + 1):
    ax.axvline(x * dx, color='lightgray', linewidth=0.7)
for y in range(Ny + 1):
    ax.axhline(y * dy, color='lightgray', linewidth=0.7)

# Draw wells
for well in st.session_state.wells:
    x = well["i"] * dx + dx / 2
    y = well["j"] * dy + dy / 2
    ax.plot(x, y, 'o', color=well["color"], markersize=10)
    ax.text(x, y + dy * 0.2, well["name"], ha='center', fontsize=9)

ax.set_xlim(0, Nx * dx)
ax.set_ylim(0, Ny * dy)
ax.set_xlabel("x (ft)")
ax.set_ylabel("y (ft)")
ax.set_title("Reservoir Grid View")
ax.set_aspect('equal')

# Hover-based coordinate display (shown separately since Streamlit can't directly hook into matplotlib events in real-time)
st.caption("ℹ️ To enable grid hover and click-to-place interaction, a JavaScript-based frontend or Plotly will be integrated in the next step.")

st.pyplot(fig)

# Display well table
st.markdown("### 💾 Current Wells")
if st.session_state.wells:
    st.dataframe(st.session_state.wells)
else:
    st.info("No wells added yet.")
