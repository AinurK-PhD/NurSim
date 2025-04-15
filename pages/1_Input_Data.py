import streamlit as st

# -----------------------------
# PAGE 1: 1_INPUT DATA
# -----------------------------
st.title("🧾 Input Data – NurSim Setup")

st.markdown("Define all parameters for the reservoir simulation. All units are in **field units**.")

# --------------------------------------
# Reservoir / Grid Properties
# --------------------------------------
st.subheader("📐 Reservoir & Grid Properties")
col1, col2, col3 = st.columns(3)

with col1:
    Nx = st.number_input("Number of grid blocks in x-direction (Nx)", min_value=1, value=10)
    dx = st.number_input("Δx – Grid block size in x (ft)", min_value=1.0, value=100.0)

with col2:
    Ny = st.number_input("Number of grid blocks in y-direction (Ny)", min_value=1, value=10)
    dy = st.number_input("Δy – Grid block size in y (ft)", min_value=1.0, value=100.0)

with col3:
    k = st.number_input("Permeability (md)", min_value=0.1, value=100.0)
    phi = st.number_input("Porosity (fraction)", min_value=0.01, max_value=1.0, value=0.2)

# --------------------------------------
# Fluid Properties (Oil & Water)
# --------------------------------------
st.subheader("🛢️ Fluid Properties (Two-Phase)")

col4, col5 = st.columns(2)

with col4:
    st.markdown("🟡 **Oil Properties**")
    mu_oil = st.number_input("Oil Viscosity μₒ (cp)", min_value=0.1, value=1.0)
    Bo = st.number_input("Oil Formation Volume Factor Bₒ (RB/STB)", min_value=0.1, value=1.2)

with col5:
    st.markdown("🔵 **Water Properties**")
    mu_water = st.number_input("Water Viscosity μ𝓌 (cp)", min_value=0.1, value=0.5)
    Bw = st.number_input("Water Formation Volume Factor B𝓌 (RB/STB)", min_value=0.1, value=1.0)

# Additional common fluid properties
st.markdown("🧪 **Common Fluid Properties**")
col6, col7 = st.columns(2)

with col6:
    ct = st.number_input("Total Compressibility ct (psi⁻¹)", min_value=1e-7, value=1e-5, format="%.1e")

with col7:
    P_init = st.number_input("Initial Reservoir Pressure (psi)", min_value=100.0, value=3000.0)



# --------------------------------------
# Simulation Time Parameters
# --------------------------------------
st.subheader("⏱️ Simulation Time Settings")
col6, col7 = st.columns(2)

with col6:
    dt = st.number_input("Time Step Δt (days)", min_value=0.1, value=10.0)

with col7:
    total_time = st.number_input("Total Simulation Time (days)", min_value=10.0, value=300.0)

# --------------------------------------
# Boundary Conditions
# --------------------------------------
st.subheader("🌐 Boundary Conditions")
boundary_type = st.selectbox("Boundary Condition Type", options=["No-flow", "Constant Pressure"])
P_boundary = None
if boundary_type == "Constant Pressure":
    P_boundary = st.number_input("Boundary Pressure (psi)", min_value=0.0, value=1000.0)





