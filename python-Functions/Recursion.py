"""
Recursion is a programming technique where a function calls itself in order to solve a problem.
It typically involves a base case to terminate the recursion and a recursive case that breaks 
the problem down into smaller subproblems.
"""

# print no 5 to 1 using recursion
def print_numbers(n):
    if n == 0:
        return
    print(n)
    print_numbers(n - 1)

print_numbers(5)

# calculate factorial of a number using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

#print all elements of a list using recursion
def print_list_elements(lst, index=0):
    if index >= len(lst):
        return
    print(lst[index] , end=' ')
    print_list_elements(lst, index + 1)

print_list_elements([1, 2, 3, 4, 5])

