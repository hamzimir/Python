# sets methods in Python (Used to perform common operations on sets)

# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)

# add() - Adds an element to the set
my_set.add(6)
print("After adding 6:", my_set)

# remove() - Removes an element from the set
my_set.remove(3)
print("After removing 3:", my_set)

# discard() - Removes an element from the set if it is a member. If not a member, do nothing
my_set.discard(10)  # 10 is not in the set, so nothing happens
print("After discarding 10 (not present):", my_set)

# pop() - Removes and returns an arbitrary element from the set
removed_element = my_set.pop()
print("After popping an element:", my_set)

# clear() - Removes all elements from the set
my_set.clear()
print("After clearing the set:", my_set)

# Recreate the set for further operations
my_set = {1, 2, 3, 4, 5}

# union() - Returns a new set with elements from both sets
another_set = {4, 5, 6, 7}
union_set = my_set.union(another_set)
print("Union of sets:", union_set)

# intersection() - Returns a new set with elements common to both sets
intersection_set = my_set.intersection(another_set)
print("Intersection of sets:", intersection_set)
