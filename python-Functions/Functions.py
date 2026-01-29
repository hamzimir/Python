"""
A function is a block of code which only runs when it is called.
A function can return data as a result.
A function helps avoiding code repetition.
Syntax to define a function in Python:
def function_name(parameters):
"""

# Example of a simple function
def greet(name):
    """This function greets the person passed as a parameter."""
    print(f"Hello, {name}!")    
# Calling the function
greet("Hamza")

# Example of a function that returns a value
def add(a, b):
    """This function returns the sum of two numbers."""
    return a + b

print(add(5, 3))  # Calling the function and returning the sum of 5 and 3