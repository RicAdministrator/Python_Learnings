# double quotation marks
print("Hello") 
print("\n")

# single quotation marks
print('Hello') 
print("\n")

# Quotes Inside Quotes
# You can use quotes inside a string, as long as they don't match the quotes surrounding the string
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
print("\n")

# Assign String to a Variable
a = "Hello"
print(a)
print("\n")

# Multiline Strings > three double quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print("\n")

# Multiline Strings > three single quotes
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
print("\n")

# Multiline Strings with Variables
x = 1
a = f"""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua. {x}
This is a test {x}"""
print(a)
print("\n")

# Strings are Arrays
# Get the character at position 1
a = "Hello, World!"
print(a[1])
print("\n")

# Looping Through a String
for x in "banana":
  print(x)
  
print("\n")

# String Length
a = "Hello, World!"
print(len(a))  
print("\n")

# To check if a certain phrase or character is present in a string, we can use the keyword in
txt = "The best things in life are free!"
print("free" in txt)
print("\n")

# Print only if "free" is present
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  
print("\n")

# Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)
print("\n")

# Use it in an if statement
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")  

print("\n")  