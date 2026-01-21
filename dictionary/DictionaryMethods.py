# Dictionary methods in Python (Used to perform common operations on dictionaries)

my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Clear() - Removes all elements from the dictionary
my_dict.clear()
print("clear my_dict:",my_dict) 

# Copy() - Returns a shallow copy of the dictionary
my_dict = {
    "name": "John", 
    "age": 30, 
    "city": "New York"  
}
copy_dict = my_dict.copy()
print("Copy of my_dict:", copy_dict)

# Fromkeys() - Returns a dictionary with the specified keys and value
keys = ("name", "age", "city")
values = ("John", 30, "New York")
my_dict = dict.fromkeys(keys, values)
print("Dictionary from keys and values:", my_dict)

# Get() - Returns the value of the specified key
age = my_dict.get("age")
print("Age:", age)

# Items() - Returns a view object that displays a list of a dictionary's key-value tuple pairs
items = my_dict.items()
print("Items in my_dict:", items)

# Keys() - Returns a view object that displays a list of a dictionary's keys
keys = my_dict.keys()
print("Keys in my_dict:", keys)

# Pop() - Removes the item with the specified key and returns its value
removed_value = my_dict.pop("city", "Not Found")
print("Removed value:", removed_value)

# Popitem() - Removes the last inserted key-value pair and returns it as a tuple
removed_item = my_dict.popitem()
print("Removed item:", removed_item)

# Setdefault() - Returns the value of the specified key. If the key does not exist, insert the key with the specified value
value = my_dict.setdefault("country", "USA")
print("Value of 'country':", value)

# Update() - Updates the dictionary with the specified key-value pairs
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
other_dict = {
    "country": "USA",
    "age": 31
}
my_dict.update(other_dict)
print("Updated my_dict:", my_dict)

# Values() - Returns a view object that displays a list of a dictionary's values
values = my_dict.values()
print("Values in my_dict:", values) 
                                
# Nested dictionary
nested_dict = {
    "name": "John",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "country": "USA"
    }
    }
print("Nested dictionary:", nested_dict)
print("Street:", nested_dict["address"]["street"])

