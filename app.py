import streamlit as st
import math

# Function to perform basic and scientific calculations
def scientific_calculate(num1, num2, operation):
    try:
        if operation == 'Add':
            return num1 + num2
        elif operation == 'Subtract':
            return num1 - num2
        elif operation == 'Multiply':
            return num1 * num2
        elif operation == 'Divide':
            if num2 == 0:
                return "Error! Division by zero."
            return num1 / num2
        elif operation == 'Power':
            return math.pow(num1, num2)
        elif operation == 'Square Root':
            if num1 < 0:
                return "Error! Cannot take the square root of a negative number."
            return math.sqrt(num1)
        elif operation == 'Logarithm (Base 10)':
            if num1 <= 0:
                return "Error! Logarithm input must be positive."
            return math.log10(num1)
        elif operation == 'Natural Logarithm (ln)':
            if num1 <= 0:
                return "Error! Logarithm input must be positive."
            return math.log(num1)
        elif operation == 'Sine':
            return math.sin(math.radians(num1))
        elif operation == 'Cosine':
            return math.cos(math.radians(num1))
        elif operation == 'Tangent':
            return math.tan(math.radians(num1))
        elif operation == 'Factorial':
            if num1 < 0 or num1 != int(num1):
                return "Error! Factorial only defined for non-negative integers."
            return math.factorial(int(num1))
        else:
            return "Invalid operation"
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit app layout
st.title("Scientific Streamlit Calculator")

# User input for the first number
num1 = st.number_input("Enter the first number", value=0.0, format="%.6f")

# User input for the second number (if needed for the operation)
num2 = st.number_input("Enter the second number (if needed)", value=0.0, format="%.6f")

# Select the operation
operation = st.selectbox("Select operation", [
    "Add", "Subtract", "Multiply", "Divide", "Power", 
    "Square Root", "Logarithm (Base 10)", "Natural Logarithm (ln)", 
    "Sine", "Cosine", "Tangent", "Factorial"
])

# Perform the calculation when the button is pressed
if st.button("Calculate"):
    result = scientific_calculate(num1, num2, operation)
    st.write(f"Result: {result}")
