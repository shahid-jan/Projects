import streamlit as st



st.set_page_config(page_title="Calculater", layout="centered")

st.title("Calculater")

num1 = st.number_input("Enter First Number", value = 0.0)
num2 = st.number_input("Enter Second Number", value = 0.0)

operation = st.selectbox(
    "Select Operation",
    ["Addition","Subtraction","Multiplication","Division"]
)

if st.button("Calculater"):
    if operation == "Addition":
      result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
          result = num1 / num2
        else:
            st.error("❌ Cannot divide by zero")
            result = None
    if result is not None:
      st.success(f"✅ Result: {result}")

# import streamlit as st

# st.set_page_config(page_title="Simple Calculator", layout="centered")

# st.title("Simple Calculator")

# num1 = st.number_input("Enter First Number", value=0.0)
# num2 = st.number_input("Enter Second Number", value=0.0)

# operation = st.selectbox(
#     "Select Operation",
#     ["Addition", "Subtraction", "Multiplication", "Division"]
# )

# if st.button("Calculate"):
#     if operation == "Addition":
#         result = num1 + num2
#     elif operation == "Subtraction":
#         result = num1 - num2
#     elif operation == "Multiplication":
#         result = num1 * num2
#     elif operation == "Division":
#         if num2 != 0:
#             result = num1 / num2
#         else:
#             st.error("❌ Cannot divide by zero")
#             result = None

#     if result is not None:
#         st.success(f"✅ Result: {result}")