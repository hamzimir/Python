#--------------Variables------------
# In Python, variables are used to store data values.
name = "Hamza"
age = 25
height = 5.9
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student:", is_student)

# ---------------Check the data type--------------
print(type(name), type(age), type(height), type(is_student))

# ---------------Type Conversion with casting--------------
# Converting data types using casting functions
name = int("5")
age = str(20)
height = bool(5.9)
is_student = float(True)

print("Type of name is:", type(name), "Type of age is:", type(age), "Type of height is:", type(height), "Type of is_student is:", type(is_student))

# --------------- Comments ---------------
# This is a single-line comment
"""This is a
multi-line comment"""   
print("Comments are important for code documentation.")

# --------------- Input ---------------
# Taking input from the user

user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
print("Name:", user_name, "Age:", user_age),print("Hello world\n")

# --------------- Input with casting ---------------

age = int(input("Enter your age: "))
height = float(input("Enter your height: "))


# practice 
# print true if a greater than or equal to b else print false
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
print(a >= b)

# Get marks from user and print grade
marks = (int(input("Enter your marks: ")))

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D") 
elif marks >= 40:
    print("Grade: E")        
else:
    print("Grade: F")

