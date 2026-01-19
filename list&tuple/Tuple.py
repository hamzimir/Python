# Tuple Methods in Python (Used to perform common operations on tuples), its similar to lists but with some differences.
# Note: Tuples are immutable, so methods that modify the tuple will return a new tuple or raise an error.
# Tuples are created using parentheses ().
# Tuples are ordered and allow duplicate values.
# for single element tuple we need to add a comma after the element like this: (element,), otherwise it will be considered as a regular parentheses.

fruits = ("apple", "banana", "cherry")
print("Original tuple:", fruits)
print("Length of tuple:", type(fruits))

# Tuple Methods

# Count() - Returns the number of times a specified value occurs in a tuple
count_banana = fruits.count("banana")
print("Count of 'banana':", count_banana)

# Index() - Returns the index of the first occurrence of a specified value in a tuple
index_cherry = fruits.index("cherry")
print("Index of 'cherry':", index_cherry)

# Note: Since tuples are immutable, methods like append(), insert(), remove(), pop(), clear(), sort(), and reverse() are not available for tuples.