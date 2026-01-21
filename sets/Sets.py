"""
 Sets in Python (Unordered collections of unique elements)
 Note: Sets are mutable, but the elements within a set must be immutable (e.g., numbers, strings, tuples).
 Sets are created using curly braces {} or the set() function.
 Sets are useful for storing unique elements, removing duplicates, and performing set operations like union, intersection, and difference.
 Sets are often used for mathematical operations like finding the union, intersection, and difference of two sets.
 List and dictonary cannot be used for these operations directly.
 """

# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)
print("Type of my_set:", type(my_set))

# sets ignore duplicate values
my_set = {1, 2, 2, 3, 4, 4, 5}
print("Set with duplicates (duplicates ignored):", my_set)

#sets are unordered
my_set = {5, 3, 1, 4, 2}
print("Set with unordered elements:", my_set)

# empty set
empty_set = set()
print("Empty set:", empty_set)

