# Example of basic arithmetic functions in Python

# Function to add two numbers
def add_numbers(a, b):
    """
    This function takes two numbers as parameters
    and returns their sum.
    """
    return a + b

# Function to subtract two numbers
def subtract_numbers(a, b):
    """
    This function takes two numbers as parameters
    and returns the difference (a - b).
    """
    return a - b

# Function to multiply two numbers
def multiply_numbers(a, b):
    """
    This function takes two numbers as parameters
    and returns their product.
    """
    return a * b

# Function to divide two numbers
def divide_numbers(a, b):
    """
    This function takes two numbers as parameters
    and returns the quotient (a / b).
    
    Note: Be careful to avoid division by zero.
    """
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

# Examples of using these functions

# Adding two numbers
result_addition = add_numbers(10, 5)
print(f"The result of addition is: {result_addition}")

# Subtracting two numbers
result_subtraction = subtract_numbers(10, 5)
print(f"The result of subtraction is: {result_subtraction}")

# Multiplying two numbers
result_multiplication = multiply_numbers(10, 5)
print(f"The result of multiplication is: {result_multiplication}")

# Dividing two numbers
result_division = divide_numbers(10, 5)
print(f"The result of division is: {result_division}")

# Trying to divide by zero
result_division_by_zero = divide_numbers(10, 0)
print(result_division_by_zero)  # Should display an error message