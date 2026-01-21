# While Loop in Python (Used to repeat a block of code as long as a certain condition is true)
#syntax:
# while condition:
#    code to be repeated


count = 0
while count <= 5:
    print("Count is:", count)
    count += 1  # Increment the counter to avoid infinite loop
print("count value:", count)

#Practice Example

# Q1 : Print numbers from 1 to 100 using a while loop.
n = 1 
while n<=100:
    print(n)
    n += 1

print("Lopp ended")    

# Q2 : Print numbers from 100 to 1 using a while loop.

n = 100 
while n>=1:
    print(n)
    n -= 1
print("Lopp ended") 

# Q3 : print a multiplication table of a given number using while loop.

n = int(input("Enter a number to print its multiplication table: "))

i = 1
while i <= 10:

    print(f"{n} x {i} = {n * i}")
    i += 1

print("Multiplication table ended")  
 
# Q4 : print the element of the following list using while loop. 
my_list = [10, 20, 30, 40, 50]

i = 0
while i < len(my_list):
    print("the volue of i is :", i, " and print the index:", i)
    print(my_list[i])
    i += 1

print("Loop ended")

""" 
Break and Continue Statement in While Loop. In Python, 'break' and 'continue' are control flow statements that can be used within
loops to modify their behavior.
The 'break' statement is used to exit the loop completely,
while the 'continue statement is used to skip the current iteration of the loop and move on to the next iteration.

syntax:
while condition:
    code to be repeated
    break
    continue
"""


# Example of break statement
n=1 
while n<=10:
    print(n)
    if n==5:
        print("Breaking the loop as n is equal to 5")
        break
    n += 1

# Q1 : search for a number x in this tuple using while loop.
numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
x = int(input("Enter a number to search in the tuple: "))
i = 0
while i < len(numbers):
    print("the value of i is:", i)
    if numbers[i] == x:
        print(f"Number {x} found at index {i}.")
        break
    i += 1
else:
    print(f"Number {x} not found in the tuple.")


# Q2 : print all the even numbers from 1 to 50 using while loop and continue statement.
n = 1
while n <= 50:
    if n % 2 != 0:
        n += 1
        continue
    print(n)
    n += 1