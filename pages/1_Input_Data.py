import streamlit as st

# -----------------------------
# PAGE 1: 1_INPUT DATA
# -----------------------------
st.title("🧾 Input Data – NurSim Setup")

st.markdown("Define all parameters for the reservoir simulation. All units are in **field units**.")

# Default values
defaults = {
    "Nx": 10, "Ny": 10, "dx": 100.0, "dy": 100.0,
    "k": 100.0, "phi": 0.2,
    "mu_oil": 1.0, "Bo": 1.2,
    "mu_water": 0.5, "Bw": 1.0,
    "ct": 1e-5, "P_init": 3000.0,
    "dt": 10.0, "total_time": 300.0,
    "boundary_type": "No-flow", "P_boundary": 1000.0
}

# Reset functionality
if st.button("🔄 Reset to Default"):
    for key, val in defaults.items():
        st.session_state[key] = val
    st.success("All fields reset to default values.")
    st.experimental_rerun()

# Load or initialize values in session state
for key, val in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = val

# --------------------------------------
# Reservoir / Grid Properties
# --------------------------------------
st.subheader("📐 Reservoir & Grid Properties")
col1, col2, col3 = st.columns(3)

with col1:
    st.session_state.Nx = st.number_input("Number of grid blocks in x-direction (Nx)", min_value=1, value=st.session_state.Nx, key="Nx_input")
    st.session_state.dx = st.number_input("Δx – Grid block size in x (ft)", min_value=1.0, value=st.session_state.dx, key="dx_input")

with col2:
    st.session_state.Ny = st.number_input("Number of grid blocks in y-direction (Ny)", min_value=1, value=st.session_state.Ny, key="Ny_input")
    st.session_state.dy = st.number_input("Δy – Grid block size in y (ft)", min_value=1.0, value=st.session_state.dy, key="dy_input")

with col3:
    st.session_state.k = st.number_input("Permeability (md)", min_value=0.1, value=st.session_state.k, key="k_input")
    st.session_state.phi = st.number_input("Porosity (fraction)", min_value=0.01, max_value=1.0, value=st.session_state.phi, key="phi_input")

# --------------------------------------
# Fluid Properties (Oil & Water)
# --------------------------------------
st.subheader("🛢️ Fluid Properties (Two-Phase)")

col4, col5 = st.columns(2)

with col4:
    st.markdown("🟡 **Oil Properties**")
    st.session_state.mu_oil = st.number_input("Oil Viscosity μₒ (cp)", min_value=0.1, value=st.session_state.mu_oil, key="mu_oil_input")
    st.session_state.Bo = st.number_input("Oil Formation Volume Factor Bₒ (RB/STB)", min_value=0.1, value=st.session_state.Bo, key="Bo_input")

with col5:
    st.markdown("🔵 **Water Properties**")
    st.session_state.mu_water = st.number_input("Water Viscosity μ𝓌 (cp)", min_value=0.1, value=st.session_state.mu_water, key="mu_water_input")
    st.session_state.Bw = st.number_input("Water Formation Volume Factor B𝓌 (RB/STB)", min_value=0.1, value=st.session_state.Bw, key="Bw_input")

# Additional common fluid properties
st.markdown("🧪 **Common Fluid Properties**")
col6, col7 = st.columns(2)

with col6:
    st.session_state.ct = st.number_input("Total Compressibility ct (psi⁻¹)", min_value=1e-7, value=st.session_state.ct, format="%.1e", key="ct_input")

with col7:
    st.session_state.P_init = st.number_input("Initial Reservoir Pressure (psi)", min_value=100.0, value=st.session_state.P_init, key="P_init_input")

# --------------------------------------
# Simulation Time Parameters
# --------------------------------------
st.subheader("⏱️ Simulation Time Settings")
col8, col9 = st.columns(2)

with col8:
    st.session_state.dt = st.number_input("Time Step Δt (days)", min_value=0.1, value=st.session_state.dt, key="dt_input")

with col9:
    st.session_state.total_time = st.number_input("Total Simulation Time (days)", min_value=10.0, value=st.session_state.total_time, key="total_time_input")

# --------------------------------------
# Boundary Conditions
# --------------------------------------
st.subheader("🌐 Boundary Conditions")
st.session_state.boundary_type = st.selectbox("Boundary Condition Type", options=["No-flow", "Constant Pressure"], index=["No-flow", "Constant Pressure"].index(st.session_state.boundary_type), key="boundary_type_input")

if st.session_state.boundary_type == "Constant Pressure":
    st.session_state.P_boundary = st.number_input("Boundary Pressure (psi)", min_value=0.0, value=st.session_state.P_boundary, key="P_boundary_input")

# --------------------------------------
# Save confirmation
# --------------------------------------
if st.button("💾 Save & Apply"):
    st.success("✅ Input data saved in session state. You can now proceed to the 2D Simulator.")
