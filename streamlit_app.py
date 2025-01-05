
import streamlit as st

# Заголовок приложения
st.title("🎈 My new app")
st.title("Выглядит говнисто")
st.write("Но что поделать")

# Простенький калькулятор
st.header("🧮 Simple usefulness for lasers")

# 1. Расчёт длины волны лазера
st.header("1. Calculation of laser wavelength")
col1, col2 = st.columns([1, 3])
with col1:
    st.image("Images/wavelength.png", caption="Laser Energy")
with col2:
    f = st.number_input("Enter the frequency (Hz):", min_value=1.0, value=1e14, step=1e12, format="%.1e")
    c = 3e8  # Скорость света (м/с)
    lambda_wave = c / f
    st.write(f"**Result:** wavelength = {lambda_wave:.3e} m")


    # 1. Расчёт длины волны лазера
st.header("1. Calculation of photon energy")
col1, col2 = st.columns([1, 3])
with col1:
    st.image("Images/photon energy.png", caption="Laser Energy")
with col2:
    f_photon = st.number_input("Enter the frequency (Hz) for the photon energy:", min_value=1.0, value=1e14, step=1e12, format="%.1e")
    h = 6.626e-34  # Постоянная Планка
    E = h * f_photon
    st.write(f"**Result:** Photon energy = {E:.2e} J")