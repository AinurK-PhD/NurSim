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
# Fluid Properties
# --------------------------------------
st.subheader("🛢️ Fluid Properties")
col4, col5 = st.columns(2)

with col4:
    mu = st.number_input("Viscosity μ (cp)", min_value=0.1, value=1.0)
    ct = st.number_input("Total compressibility ct (psi⁻¹)", min_value=1e-7, value=1e-5, format="%.1e")

with col5:
    Bo = st.number_input("Formation Volume Factor Bo (RB/STB)", min_value=0.1, value=1.2)
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





