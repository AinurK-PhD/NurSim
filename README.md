# 🛢️ NurSim – 2D Reservoir Simulation App

**NurSim** is an interactive, browser-based reservoir simulator for **2D two-phase (oil-water) flow**, built using Python and Streamlit. It is designed for educational and research purposes, focusing on field-unit input, well placement, and simulation using the **IMPES method** (Implicit Pressure, Explicit Saturation).
P.S. Development is currently on hold due to Python's limitations in efficiently handling full-field reservoir flow simulations, but may be resumed in the future.

---

## 🚀 Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ainurk-phd-nursim-home-3zvxhf.streamlit.app/)

---

## 📦 Features

- 🧾 **Input Page** – Define all reservoir and fluid properties in field units  
- ⛽ **Well Placement & Configuration** – Add injectors and producers with location and rate control  
- 💻 **Simulation Engine** – Two-phase IMPES-based pressure & saturation simulator  
- 📊 **Results Visualization** *(coming soon)* – Pressure and saturation maps with well overlays  
- 🌐 **Streamlit App** – Deployed on the cloud, accessible from any device  

---

## 📁 Project Structure


NurSim/ 

├── Home.py # Main entry page (welcome/info) 

├── pages/ 

    ├── 1_Input_Data.py # Reservoir and fluid properties input 
  
    ├── 2_Results.py # Results page (coming soon) 
  
├── requirements.txt # Python dependencies



---

## 🧠 Purpose

This app is developed as part of an **Advanced Reservoir Simulation** term project at **KFUPM**, with the goal of building an intuitive, minimal, and engineering-focused simulator using modern interactive tools.

---

## 📚 Further Reading & Tools

- [Streamlit Documentation](https://docs.streamlit.io)
- [Numerical Reservoir Simulation – FDM/IMPES Basics](https://petrowiki.spe.org/Numerical_reservoir_simulation)
- [Reservoir Engineering with Python (GitHub)](https://github.com/rouseguy/Reservoir-Engineering)

---

## 👤 Author

**Ainur Khakimov**, PhD Candidate  
Reservoir Engineering & AI  
King Fahd University of Petroleum and Minerals (KFUPM)  
[GitHub: AinurK-PhD](https://github.com/AinurK-PhD)

---

