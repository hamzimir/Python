# in python we used different operations on files like reading , writing , appending etc

# File Handling in Python
# Open a file
file = open("demo.txt", "r")  # 'r' mode for reading
data = file.read()  # Read the content of the file
print(data)  # Print the content
print(type(data))  # Print the type of data read from file
file.close()  # Close the file
#--------------------------------------------------

# Writing to a file
file = open("demo.txt", "w")  # 'w' mode for writing (will overwrite existing content)
file.write("Hello, World!\n")  # Write a string to the file
file.write("This is a demo file.\n")  # Write another string
file.close()  # Close the file

#--------------------------------------------------

# Appending to a file
file = open("demo.txt", "a")  # 'a' mode for appending
file.write("Appending a new line.\n")  # Append a new line to the file
file.close()  # Close the file

#--------------------------------------------------

# Reading file line by line
file = open("demo.txt", "r")  # Open the file in read mode
for line in file:
    print(line.strip())  # Print each line without extra newlines
file.close()  # Close the file

#--------------------------------------------------

# Using 'with' statement for file operations
with open("demo.txt", "r") as file:
    content = file.read()  # Read the content of the file
    print(content)  # Print the content
# No need to explicitly close the file, it's done automatically

#--------------------------------------------------

# Checking if file exists before reading
import os   
if os.path.exists("demo.txt"):
    with open("demo.txt", "r") as file:
        print(file.read())
else:
    print("File does not exist.")

# Note: Make sure to handle exceptions in real-world applications for better error management.
# in python we used different operations on files like reading , writing , appending etc
# File Handling in Python
# Open a file 

#--------------------------------------------------
import os
# remove file from the system
os.remove("demo.txt") 

#--------------------------------------------------

"""
File handling is an important part of any web application.
Python has several functions for creating, reading, updating, and deleting files.
There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
"""