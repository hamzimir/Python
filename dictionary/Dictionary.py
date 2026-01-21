# Dictionary is used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Dictionaries are written with curly brackets, and they have keys and values.
# Note: As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
""" When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
 Unordered means that the items do not have a defined order, you cannot refer to an item by using an index."""


# Creating a dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print("Original dictionary:", my_dict)

print("Length of dictionary:", len(my_dict))
print("Type of my_dict:", type(my_dict))
print("Keys of my_dict:", my_dict.keys())
print("Values of my_dict:", my_dict.values())
print("key value of name", my_dict["name"])


# Adding an item to the dictionary
my_dict["country"] = "USA"
my_dict["age"] = 31  # Updating an existing key
print("Updated dictionary:", my_dict)

#nested dictionary
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
