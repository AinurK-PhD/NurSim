import streamlit as st

st.set_page_config(page_title="NurSim", page_icon="🏠", layout="wide")

st.title("NurSim: A Basic Reservoir Simulation App")

st.info("""
Welcome to **NurSim** – a 2D Interactive Reservoir Simulator based on the **IMPES method** (Implicit Pressure, Explicit Saturation) for two-phase (oil-water) flow.

🔍 **Features:**
- Customizable 2D grid for reservoir modeling
- Add injectors and producers interactively
- Simulate two-phase flow using IMPES (pressure & saturation fields)
- Visualize pressure and saturation maps with well markers

🛠️ **Built with:**
- Python 🐍
- Streamlit 🌐
- NumPy & Matplotlib 📊

🧠 **Created by:** Ainur Khakimov (PhD Candidate, Department of Petroleum Engineering)  
👨‍🏫 **Supervised by:** Dr. Mohammad Sarim Jamal (Instructor, Department of Petroleum Engineering)  
📁 [GitHub Repository](https://github.com/AinurK-PhD/NurSim)
""")
