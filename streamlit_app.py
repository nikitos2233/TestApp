
import streamlit as st
import math as mt
# Заголовок приложения

col1, col2 = st.columns([1, 3])
with col2: st.title("🎈 My little Calc")
st.header("🧮 Simple usefulness for lasers")

# Laser wave
st.header("1. Calculation of laser wavelength")
col1, col2 = st.columns([1, 3])
with col1:
    formula = r"\lambda = \frac{c}{f}"
    st.latex(formula)
with col2:
    f = st.number_input("Enter the frequency (Hz):", min_value=1.0, value=1e14, step=1e12, format="%.1e")
    c = 3e8  # Light const (m/s)
    lambda_wave = c / f
    st.write(f"**Result:** wavelength = {lambda_wave:.3e} m")


# Photon Energy
st.header("2. Calculation of photon energy")
col1, col2 = st.columns([1, 3])
with col1:

    formula = r"E= {h} {f}"
    st.latex(formula)
with col2:
    f_photon = st.number_input("Enter the frequency (Hz) for the photon energy:", min_value=1.0, value=1e14, step=1e12, format="%.1e")
    h = 6.626e-34  # Plank  const
    E = h * f_photon
    st.write(f"**Result:** Photon energy = {E:.2e} J")

# Power density
st.header("3. Calculation of laser power density")
col1, col2 = st.columns([1, 3])
with col1:
    formula = r"I= \frac{P}{A}"
    st.latex(formula)
with col2:
    P = st.number_input("Enter the laser power (W):", min_value=0.0, value=10.0, step=1.0)
    A = st.number_input("Enter the cross-sectional area of the beam (m²):", value=1e-4, format="%.1e")
    I = P / A
    st.write(f"**Result:** Power density = {I:.2e} W/m²")

# Losses to dB
st.header("4. Light absolut Power losses to dB")
col1, col2, col3 = st.columns([3,1,1])
with col1:
    formula = r"L = 10 \cdot \log_{10}\left(\frac{P_{\text{вх}}}{P_{\text{вых}}}\right)"
    st.latex(formula)
with col2: 
    P_in = st.number_input("Input Power (mW)", min_value=0.0, step=0.1)
with col3:
    P_out = st.number_input("Output Power (mW)", min_value=0.0, step=0.1)
if P_in > 0 and P_out > 0:
    L = 10 * mt.log10(P_in / P_out)
    st.success(f"losses: {L:.2f} dB")
else:
    st.warning("Enter both values greater than 0")    