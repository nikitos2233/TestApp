
import streamlit as st

# Заголовок приложения

col1, col2 = st.columns([1, 3])
with col2: st.title("🎈 My little Calc")
st.header("🧮 Simple usefulness for lasers")

# Laser wave
st.header("1. Calculation of laser wavelength")
col1, col2 = st.columns([1, 3])
with col1:
    st.image("Images/wavelength.png", caption="Laser Energy")
with col2:
    f = st.number_input("Enter the frequency (Hz):", min_value=1.0, value=1e14, step=1e12, format="%.1e")
    c = 3e8  # Light const (m/s)
    lambda_wave = c / f
    st.write(f"**Result:** wavelength = {lambda_wave:.3e} m")


# Photon Energy
st.header("2. Calculation of photon energy")
col1, col2 = st.columns([1, 3])
with col1:
    st.image("Images/photon energy.png", caption="Photon Energy")
with col2:
    f_photon = st.number_input("Enter the frequency (Hz) for the photon energy:", min_value=1.0, value=1e14, step=1e12, format="%.1e")
    h = 6.626e-34  # Plank  const
    E = h * f_photon
    st.write(f"**Result:** Photon energy = {E:.2e} J")

# Power density
st.header("3. Calculation of laser power density")
col1, col2 = st.columns([1, 3])
with col1:
    st.image("Images/power density.png", caption="Power Density")
with col2:
    P = st.number_input("Enter the laser power (W):", min_value=0.0, value=10.0, step=1.0)
    A = st.number_input("Enter the cross-sectional area of the beam (m²):", value=1e-4, format="%.1e")
    I = P / A
    st.write(f"**Result:** Power density = {I:.2e} W/m²")