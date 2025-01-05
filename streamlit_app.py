
import streamlit as st

# Заголовок приложения
st.title("🎈 My new app")
st.title("Выглядит говнисто")
st.write("Но что поделать")

# Простенький калькулятор
st.header("🧮 Simple usefulness for lasers")


# 1. Расчёт длины волны лазера
st.header("Calculation of laser wavelength")

st.image("images/energy.png", caption="Laser Energy")
f = st.number_input("Enter the frequency (Hz):", min_value=1.0, value=1e14, step=1e12, format="%.1e")
c = 3e8  # Скорость света (м/с)
lambda_wave = c / f
st.write(f"**Результат:** Длина волны = {lambda_wave:.2e} м")

# 2. Расчёт энергии фотона
st.header("2. Расчёт энергии фотона")
f_photon = st.number_input("Введите частоту (Гц) для энергии фотона:", min_value=1.0, value=1e14, step=1e12, format="%.1e")
h = 6.626e-34  # Постоянная Планка (Дж·с)
E = h * f_photon
st.write(f"**Результат:** Энергия фотона = {E:.2e} Дж")

# 3. Расчёт плотности мощности лазера
st.header("3. Расчёт плотности мощности лазера")
P = st.number_input("Введите мощность лазера (Вт):", min_value=0.0, value=10.0, step=1.0)
A = st.number_input("Введите площадь сечения пучка (м²):", min_value=1e-6, value=1e-4, step=1e-6, format="%.1e")
I = P / A
st.write(f"**Результат:** Плотность мощности = {I:.2e} Вт/м²")

st.write("Приложение готово для проверки трёх формул!")

