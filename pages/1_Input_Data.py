import streamlit as st

# -----------------------------
# PAGE 1: 1_INPUT DATA
# -----------------------------
st.title("🧾 Input Data – NurSim Setup")
st.markdown("Define all parameters for the reservoir simulation. All units are in **field units**.")


if st.session_state.get("reset_triggered", False):
    st.session_state["reset_triggered"] = False
    st.rerun()



# -----------------------------
# Default values
# -----------------------------
defaults = {
    "Nx": 10, "Ny": 10, "dx": 100.0, "dy": 100.0,
    "k": 100.0, "phi": 0.2,
    "mu_oil": 1.0, "Bo": 1.2,
    "mu_water": 0.5, "Bw": 1.0,
    "ct": 1e-5, "P_init": 3000.0,
    "dt": 10.0, "total_time": 300.0,
    "boundary_type": "No-flow", "P_boundary": 1000.0
}

for key, val in defaults.items():
    st.session_state.setdefault(key, val)

# --------------------------------------
# Reservoir / Grid Properties
# --------------------------------------
st.subheader("📐 Reservoir & Grid Properties")
col1, col2, col3 = st.columns(3)
with col1:
    Nx = st.number_input("Number of grid blocks in x-direction (Nx)", min_value=1, value=st.session_state["Nx"], key="input_Nx")
    dx = st.number_input("Δx – Grid block size in x (ft)", min_value=1.0, value=st.session_state["dx"], key="input_dx")
with col2:
    Ny = st.number_input("Number of grid blocks in y-direction (Ny)", min_value=1, value=st.session_state["Ny"], key="input_Ny")
    dy = st.number_input("Δy – Grid block size in y (ft)", min_value=1.0, value=st.session_state["dy"], key="input_dy")
with col3:
    k = st.number_input("Permeability (md)", min_value=0.1, value=st.session_state["k"], key="input_k")
    phi = st.number_input("Porosity (fraction)", min_value=0.01, max_value=1.0, value=st.session_state["phi"], key="input_phi")

# --------------------------------------
# Fluid Properties (Oil & Water)
# --------------------------------------
st.subheader("🛢️ Fluid Properties (Two-Phase)")
col4, col5 = st.columns(2)
with col4:
    st.markdown("🟡 **Oil Properties**")
    mu_oil = st.number_input("Oil Viscosity μₒ (cp)", min_value=0.1, value=st.session_state["mu_oil"], key="input_mu_oil")
    Bo = st.number_input("Oil Formation Volume Factor Bₒ (RB/STB)", min_value=0.1, value=st.session_state["Bo"], key="input_Bo")
with col5:
    st.markdown("🔵 **Water Properties**")
    mu_water = st.number_input("Water Viscosity μ𝓌 (cp)", min_value=0.1, value=st.session_state["mu_water"], key="input_mu_water")
    Bw = st.number_input("Water Formation Volume Factor B𝓌 (RB/STB)", min_value=0.1, value=st.session_state["Bw"], key="input_Bw")

# Common fluid properties
st.markdown("🧪 **Common Fluid Properties**")
col6, col7 = st.columns(2)
with col6:
    ct = st.number_input("Total Compressibility ct (psi⁻¹)", min_value=1e-7, value=st.session_state["ct"], format="%.1e", key="input_ct")
with col7:
    P_init = st.number_input("Initial Reservoir Pressure (psi)", min_value=100.0, value=st.session_state["P_init"], key="input_P_init")

# --------------------------------------
# Simulation Time
# --------------------------------------
st.subheader("⏱️ Simulation Time Settings")
col8, col9 = st.columns(2)
with col8:
    dt = st.number_input("Time Step Δt (days)", min_value=0.1, value=st.session_state["dt"], key="input_dt")
with col9:
    total_time = st.number_input("Total Simulation Time (days)", min_value=10.0, value=st.session_state["total_time"], key="input_total_time")

# --------------------------------------
# Boundary Conditions
# --------------------------------------
st.subheader("🌐 Boundary Conditions")
boundary_type = st.selectbox("Boundary Condition Type", options=["No-flow", "Constant Pressure"],
                             index=["No-flow", "Constant Pressure"].index(st.session_state["boundary_type"]), key="input_boundary_type")

P_boundary = st.session_state["P_boundary"]
if boundary_type == "Constant Pressure":
    P_boundary = st.number_input("Boundary Pressure (psi)", min_value=0.0, value=st.session_state["P_boundary"], key="input_P_boundary")

# --------------------------------------
# Buttons at bottom: Reset + Save
# --------------------------------------
col_save, col_reset = st.columns(2)

with col_save:
    if st.button("💾 Save & Apply"):
        st.session_state.update({
            "Nx": Nx, "Ny": Ny, "dx": dx, "dy": dy,
            "k": k, "phi": phi,
            "mu_oil": mu_oil, "Bo": Bo,
            "mu_water": mu_water, "Bw": Bw,
            "ct": ct, "P_init": P_init,
            "dt": dt, "total_time": total_time,
            "boundary_type": boundary_type,
            "P_boundary": P_boundary
        })
        st.success("✅ Input data saved in session state. You can now proceed to the 2D Simulator.")

with col_reset:
    if st.button("🔄 Reset to Default"):
        for key, val in defaults.items():
            st.session_state[key] = val
        st.session_state["reset_triggered"] = True
        st.success("All fields reset to default values.")

