# identity Operators (Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:)

# i-is operator (is: returns False because x is not the same object as y, even if they have the same content)
x = ["apple", "banana", "cherry"]   
y = ["apple", "banana", "cherry"]
print("x is y:", x is y)

# ii-is not operator (is not: returns True because x is not the same object as y, even if they have the same content)
x = ["apple", "banana", "cherry"]   
y = ["apple", "banana", "cherry"]       
print("x is not y:", x is not y)    

# ii-is operator (is: returns True because z is the same object as x)
x = ["apple", "banana", "cherry"]   
y = ["apple", "banana", "cherry"] 
z = x      
print("x is y:", x is z)