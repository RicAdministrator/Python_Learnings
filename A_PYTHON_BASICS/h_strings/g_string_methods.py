# capitalize() - Converts the first character to upper case
txt = "michael"
x = txt.capitalize()
print(x)

# casefold() - Converts string into lower case
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

# center() - Returns a centered string
# Print the word "banana", taking up the space of 20 characters, with "banana" in the middle
txt = "banana"
x = txt.center(20)
print("12345678901234567890")
print(x)

# count() - Returns the number of times a specified value occurs in a string
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

# encode() - Returns an encoded version of the string
# UTF-8 encode the string
txt = "My name is Ståle"
x = txt.encode()
print(x) # Output: b'My name is St\xc3\xa5le'

# endswith() - Returns true if the string ends with the specified value
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

# To Do: Add more string methods