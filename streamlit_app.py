
import streamlit as st

# Заголовок приложения
st.title("🎈 My new app")
st.title("Выглядит говнисто")
st.write("Но что поделать")

# Простенький калькулятор
st.header("🧮 Простенький калькулятор")

# Поля для ввода чисел
num1 = st.number_input("Введите первое число", value=0.0)
num2 = st.number_input("Введите второе число", value=0.0)

# Выбор операции
operation = st.selectbox(
    "Выберите операцию",
    ("Сложение", "Вычитание", "Умножение", "Деление")
)

# Кнопка для выполнения операции
if st.button("Вычислить"):
    if operation == "Сложение":
        result = num1 + num2
        st.success(f"Результат: {result}")
    elif operation == "Вычитание":
        result = num1 - num2
        st.success(f"Результат: {result}")
    elif operation == "Умножение":
        result = num1 * num2
        st.success(f"Результат: {result}")
    elif operation == "Деление":
        if num2 != 0:
            result = num1 / num2
            st.success(f"Результат: {result}")
        else:
            st.error("Ошибка: Деление на ноль!")

