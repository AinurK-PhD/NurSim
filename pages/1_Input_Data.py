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

# Initialize session state (without triggering widget key conflict warnings)
for key, val in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = val

# Temporary variables for form inputs
Nx_val = st.session_state.Nx
Ny_val = st.session_state.Ny
dx_val = st.session_state.dx
dy_val = st.session_state.dy
k_val = st.session_state.k
phi_val = st.session_state.phi
mu_oil_val = st.session_state.mu_oil
Bo_val = st.session_state.Bo
mu_water_val = st.session_state.mu_water
Bw_val = st.session_state.Bw
ct_val = st.session_state.ct
P_init_val = st.session_state.P_init
dt_val = st.session_state.dt
total_time_val = st.session_state.total_time
boundary_type_val = st.session_state.boundary_type
P_boundary_val = st.session_state.P_boundary

# --------------------------------------
# Reservoir / Grid Properties
# --------------------------------------
st.subheader("📐 Reservoir & Grid Properties")
col1, col2, col3 = st.columns(3)

with col1:
    Nx_val = st.number_input("Number of grid blocks in x-direction (Nx)", min_value=1, value=Nx_val)
    dx_val = st.number_input("Δx – Grid block size in x (ft)", min_value=1.0, value=dx_val)

with col2:
    Ny_val = st.number_input("Number of grid blocks in y-direction (Ny)", min_value=1, value=Ny_val)
    dy_val = st.number_input("Δy – Grid block size in y (ft)", min_value=1.0, value=dy_val)

with col3:
    k_val = st.number_input("Permeability (md)", min_value=0.1, value=k_val)
    phi_val = st.number_input("Porosity (fraction)", min_value=0.01, max_value=1.0, value=phi_val)

# --------------------------------------
# Fluid Properties (Oil & Water)
# --------------------------------------
st.subheader("🛢️ Fluid Properties (Two-Phase)")

col4, col5 = st.columns(2)

with col4:
    st.markdown("🟡 **Oil Properties**")
    mu_oil_val = st.number_input("Oil Viscosity μₒ (cp)", min_value=0.1, value=mu_oil_val)
    Bo_val = st.number_input("Oil Formation Volume Factor Bₒ (RB/STB)", min_value=0.1, value=Bo_val)

with col5:
    st.markdown("🔵 **Water Properties**")
    mu_water_val = st.number_input("Water Viscosity μ𝓌 (cp)", min_value=0.1, value=mu_water_val)
    Bw_val = st.number_input("Water Formation Volume Factor B𝓌 (RB/STB)", min_value=0.1, value=Bw_val)

# Additional common fluid properties
st.markdown("🧪 **Common Fluid Properties**")
col6, col7 = st.columns(2)

with col6:
    ct_val = st.number_input("Total Compressibility ct (psi⁻¹)", min_value=1e-7, value=ct_val, format="%.1e")

with col7:
    P_init_val = st.number_input("Initial Reservoir Pressure (psi)", min_value=100.0, value=P_init_val)

# --------------------------------------
# Simulation Time Parameters
# --------------------------------------
st.subheader("⏱️ Simulation Time Settings")
col8, col9 = st.columns(2)

with col8:
    dt_val = st.number_input("Time Step Δt (days)", min_value=0.1, value=dt_val)

with col9:
    total_time_val = st.number_input("Total Simulation Time (days)", min_value=10.0, value=total_time_val)

# --------------------------------------
# Boundary Conditions
# --------------------------------------
st.subheader("🌐 Boundary Conditions")
boundary_type_val = st.selectbox("Boundary Condition Type", options=["No-flow", "Constant Pressure"], index=["No-flow", "Constant Pressure"].index(boundary_type_val))
P_boundary_val = None
if boundary_type_val == "Constant Pressure":
    P_boundary_val = st.number_input("Boundary Pressure (psi)", min_value=0.0, value=P_boundary_val or 1000.0)

# --------------------------------------
# Buttons
# --------------------------------------
col_btn1, col_btn2 = st.columns([1, 1])

with col_btn1:
    if st.button("💾 Save & Apply"):
        st.session_state.Nx = Nx_val
        st.session_state.Ny = Ny_val
        st.session_state.dx = dx_val
        st.session_state.dy = dy_val
        st.session_state.k = k_val
        st.session_state.phi = phi_val
        st.session_state.mu_oil = mu_oil_val
        st.session_state.Bo = Bo_val
        st.session_state.mu_water = mu_water_val
        st.session_state.Bw = Bw_val
        st.session_state.ct = ct_val
        st.session_state.P_init = P_init_val
        st.session_state.dt = dt_val
        st.session_state.total_time = total_time_val
        st.session_state.boundary_type = boundary_type_val
        st.session_state.P_boundary = P_boundary_val
        st.success("✅ Input data saved in session state. You can now proceed to the 2D Simulator.")

with col_btn2:
    if st.button("🔄 Reset to Default"):
        for key, val in defaults.items():
            st.session_state[key] = val
        st.success("All fields reset to default values.")
        st.rerun()
