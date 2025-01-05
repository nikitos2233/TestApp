
import streamlit as st

# Заголовок приложения
st.title("🎈 My new app")
st.title("Выглядит говнисто")
st.write("Но что поделать")

# Простенький калькулятор
st.header("🧮 Simple usefulness for lasers")

# 1. Расчёт длины волны лазера
col1, col2 = st.columns([1, 3])
with col1:
    st.image("Images/energy.png", caption="Laser Energy", use_container_width=True)
with col2:
    st.header("1. Расчёт длины волны лазера")
    f = st.number_input("Введите частоту (Гц):", min_value=1.0, value=1e14, step=1e12, format="%.1e")
    c = 3e8  # Скорость света (м/с)
    lambda_wave = c / f
    st.write(f"**Результат:** Длина волны = {lambda_wave:.2e} м")