# String functions (used for manipulating and working with strings)

def string_functions():
    sample_string = " Hello, World! Welcome to Python Programming. "

    # 1. Length of the string
    length = len(sample_string)
    print("Length of the string:", length)

    # 2. Convert to uppercase
    upper_string = sample_string.upper()
    print("Uppercase string:", upper_string)

    # 3. Convert to lowercase
    lower_string = sample_string.lower()
    print("Lowercase string:", lower_string)

    # 4. Strip whitespace from both ends
    stripped_string = sample_string.strip()
    print("Stripped string:", stripped_string)

    # 5. Replace a substring
    replaced_string = sample_string.replace("World", "Universe")
    print("Replaced string:", replaced_string)

    # 6. Find a substring
    index = sample_string.find("Python")
    print("Index of 'Python':", index)

    # 7. Split the string into a list of words
    split_string = sample_string.split(" ")
    print("Split string:", split_string)

# Call the function to see the results
string_functions()

# Note: Strings are immutable in Python, meaning once created, they cannot be changed. Any operation that modifies a string will create a new string.


# Practice: get input from user firstname and find its length

# firstname = (str(input("Enter your first name: "))).upper()
# print("Your first name is:", firstname, "Length of your first name is:", len(firstname))

# Practice: find and  count of "$" in a string and replace it with "USD"

currency_string = ("I have 100$ in my wallet.").find("$")
print(currency_string)
count_string = ("I have 100$ in my wallet.").count("$")
print(count_string)
replace_string = ("I have 100$ in my wallet.").replace("$", "USD")
print(replace_string)