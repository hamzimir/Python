"""
Attrubute & Method
Attribute is a variable that is associated with an object
Any data or properteis of an object is called attribute
Method is a function that is associated with an object
Any behavior of an object is called method
"""

#example pf attribute

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

my_car = Car("Honda", "Civic", 2022)
print(my_car.make)
print(my_car.model)
print(my_car.year)

#example of method

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person = Person("John", 30)
person.introduce()


# Q1: create student class that takes name and marks of three subjects and calculate average marks

class Student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def calculate_average(self):
        return (self.marks1 + self.marks2 + self.marks3) / 3
    
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Marks 1: {self.marks1}")
        print(f"Marks 2: {self.marks2}")
        print(f"Marks 3: {self.marks3}")
        print(f"Average Marks: {self.calculate_average()}")

student = Student("Hamza", 90, 80, 70)
student.display_details()

# ---------------------------------------------

"""
Static method:
A static method is a method that is associated with a class and not with an object of that class.
It is a class method that is called without creating an object of the class.
Static methods are defined using the @staticmethod decorator.
In static method we dont need "self" parameter.
Without decorator we get error
"""

class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method")

MyClass.static_method()

# ------------------------------------------

# del keyword:-  del keyword is used to delete an attribute or method of a class and 
# it also delete whole class

class MyClass:
    students = 10
    def instance_method(self):
     print("This is an instance method")

obj = MyClass()
del obj.student
del obj.instance_method

