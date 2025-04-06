import streamlit as st
from st_pages import Page, show_pages, add_page_title

st.set_page_config(page_title="NurSim", page_icon="🏠", layout="wide")

# Adds this page’s title to the sidebar
add_page_title()

# Show custom sidebar labels/icons
show_pages(
    [
        Page("streamlit_app.py", "Home", "🏠"),
        Page("pages/1_Input_Data.py", "Input Data", "🧾"),
        # You can add more pages here later
    ]
)

st.title("NurSim: A Basic Reservoir Simulation App")

st.info("""
**Welcome to NurSim** – a simple 2D reservoir simulator built using Finite Difference Methods (FDM).

🔍 **Features**:
- Customizable 2D grid for reservoir modeling
- Add injectors and producers interactively
- Simulate single-phase pressure distribution over time
- Visualize pressure fields and well effects

🛠️ **Built with**:
- Python 🐍
- Streamlit 🌐
- NumPy & Matplotlib 📊

🧠 **Created by:** Ainur Khakimov (PhD Candidate – Reservoir Engineering)

📁 [GitHub Repository](https://github.com/AinurK-PhD/NurSim)
""")
