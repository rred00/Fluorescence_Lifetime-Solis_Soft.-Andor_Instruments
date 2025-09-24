# Fluorescence Lifetime Imaging (FLIM) Plotting Toolkit

This repository contains Python scripts for plotting **Time-Resolved Photoluminescence (TRPL)** and **Fluorescence Lifetime Imaging Microscopy (FLIM)** data.  
It is designed to help researchers visualize experimental lifetime data using simple, customizable plots.

⚠️ **Note**: This will work only for the generated ASCII file from **ANDOR Instruments U.K.**

---

## ✨ Features
- Plot TRPL decay curves from experimental data.
- Visualize FLIM lifetime maps with customizable colormaps.
- Adjustable fitting options (single/multi-exponential).
- Easy to modify and extend for specific experimental setups.

---

## 📂 Repository Structure
- `codes/` → Python scripts for data processing and analysis  
- `docs/` → Experiment details, schematics, and notes  
- `README.md` → Overview of the project  

---

## 🧪 Experiment Details
The experiment involves wide-field fluorescence lifetime imaging of **Rh6G**.  
The setup is based on [objective lens, excitation source, detection method].  

Detailed notes are available in [`docs/experiment_details.md`](docs/experiment_details.md).

---

## 🖼️ Schematic
Below is the experimental schematic:

![Experimental Schematic](docs/schematic.png)

---

## 💻 Code Usage
Clone the repository:
```bash
git clone https://github.com/<your-username>/<repo-name>.git
