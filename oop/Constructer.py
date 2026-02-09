"""
constructer is a special method that is called when an object is created
constructer is used to initialize the object
it is called automatically when an object is created
"""
class MyClass:
    def __init__(self):
        print("Hello World")

p1 = MyClass()
print(p1)

# update name by using ocnstructer of class
class Student:
    name = "Ali"
    def __init__(self, Myname):
        print(self)
        self.name = Myname
p1 = Student("Hamza")
print(p1)
print(p1.name)