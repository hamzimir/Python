# List Methods (Used to perform common operations on lists)

fruits = ["apple", "banana", "cherry"]

# Append() - Adds an item to the end of the list
fruits.append("orange")
print("append fruits orange:",fruits)

# Insert() - Adds an item at the specified index
fruits.insert(1, "kiwi")
print("insert fruits kiwi:",fruits)

# Remove() - Removes an item from the list
fruits.remove("banana")
print("remove fruits banana:",fruits)

# Pop() - Removes the item at the specified index (default is the last item)
popped_fruit = fruits.pop()
print("pop fruits:",fruits)
print("popped fruit:",popped_fruit)

# Clear() - Removes all items from the list
fruits.clear()
print("clear fruits:",fruits)   

# Note: After clear(), the list is empty. To demonstrate other methods, we need to reinitialize the list.
fruits = ["apple", "banana", "cherry"]

# Sort() - Sorts the list in ascending order
fruits.sort()
print("sort fruits:",fruits)

# Sort() - Sorts the list in descending order
fruits.sort(reverse=True)
print("reverse sort fruits:",fruits)

# Reverse() - Reverses the order of the list
fruits.reverse()
print("reverse fruits:",fruits)

# practice

# Q1: Ask user to enter 3 colors and store them in a list. Then, sort the list in alphabetical order and print it.
user_colors = []

first_color = input("Enter first color: ")
second_color = input("Enter second color: ")
third_color = input("Enter third color: ")

user_colors.append(first_color)
user_colors.append(second_color)
user_colors.append(third_color)

user_colors.sort()
print("Sorted list:", user_colors)  

# Q2: Check list contain element of palindrome or not and print it. (palindrome means same word when read from front or backward (reverse) same like madam, level, radar etc.).


num1 = [1,2,1]
num2 = [1,2,3]

copy_num1 = num1.copy()
print("copy_num1 before modification:",copy_num1)
copy_num1.reverse()
print("copy_num1 after reverse:",copy_num1)

copy_num2 = num2.copy()
print("copy_num2 before modification:",copy_num2)
copy_num2.reverse()
print("copy_num2 after reverse:",copy_num2)

if num1 == copy_num1:
    print("num1 is palindrome")
else:
    print("num1 is not palindrome")

if num2 == copy_num2:
    print("num2 is palindrome")    
else:
    print("num2 is not palindrome")
