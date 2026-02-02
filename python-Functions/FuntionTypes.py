"""
there are two types of functions in python
1. Built-in functions
2. User-defined functions
"""

""""
Built-in functions are pre-defined functions in python that can be used directly without any need of definition.
Examples of built-in functions: print(), len(), type(), int(), str(), etc.
"""

"""
User-defined functions are functions that are defined by the user to perform specific tasks.  
Examples of user-defined functions are given in the Functions.py file. 
"""


# practice Questions on functions:
# Q1 : Write a function to find the maximum of three numbers.
def max_of_three(a, b, c):
    """This function returns the maximum of three numbers."""
    return max(a, b, c)
print(max_of_three(10, 20, 15))  # Output: 20

# Q2 : Write a function to check if a number is prime.
def is_prime(n):
    """This function checks if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
    
        if n % i == 0:
            return False
    return True

print(is_prime(10))  

# def is_prime_verbose(n):
#     if n <= 1:
#         print(f"{n} prime nahi hai (0 ya 1 prime nahi hotay)")
#         return False

#     print(f"{n} ka prime check start ho raha hai...\n")

#     for i in range(2, int(n**0.5) + 1):
#         print(f"Iteration: i = {i}")
#         print(f"{n} % {i} = {n % i}")

#         if n % i == 0:
#             print(f"\nResult: {n} prime nahi hai, kyun ke {i} se divide ho jata hai.")
#             return False

#         print("Divide nahi hua, next iteration...\n")

#     print(f"\nFinal Result: {n} prime number hai ✅")
#     return True
# print(is_prime_verbose(29))                 

# ---------------------------------------------------------
# Q3 : Write a function to calculate the factorial of a number.

def calculate_factorial(n):

    fact = 1

    for i in range(1, n + 1):
        print(i)
        fact *= i  #fact = fact * i
        print(fact)
    print(fact)

calculate_factorial(5)  

# def calculate_factorial(n):

#     fact = 1

#     print(f"Calculating factorial of {n}:\n")

#     for i in range(1, n + 1):
        
#         fact *= i  # fact = fact * i
#         print(f"Iteration {i}: value of i = {i} → current factorial = {fact}")

#     print(f"\nFinal factorial of {n} is: {fact}")

# calculate_factorial(5)

# Q4 : Write a function to convert pounds to pkr.

def Converter(pounds):
    """Convert pounds to Pakistani Rupees."""
    pkr = pounds * 383
    return pkr

# -------------- OR--------------------------------
def pounds_to_pkr(pounds, exchange_rate=383):
    """Convert pounds to Pakistani Rupees."""
    return pounds * exchange_rate

print(pounds_to_pkr(10))  # Output: 2000

# Q5 : Write a function to check input no is even or odd.
def is_even_or_odd(n):
    """Check if a number is even or odd."""
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

n = input("Enter a number: ")
n = int(n)
print(is_even_or_odd(n))  # Output: Even or Odd depending on input