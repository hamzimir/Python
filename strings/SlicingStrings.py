# Slicing Strings in Python (Used to extract a part of a string)

name = "HAMZA Shafique"
print(name[0:5])
print(name[6:15])
print(name[:5])    # From start to index 5
print(name[6:])    # From index 6 to end

# Note: The end index is exclusive, meaning the character at that index is not included in the result.

#-------------------------------------------------

#  Negative Indexing (Used to access characters from the end of a string)

name = "HAMZA Shafique"
print(name[-5:-1])
print(name[-8:])    # From index -7 to end
print(name[:-8   ])    # From start to index -5



