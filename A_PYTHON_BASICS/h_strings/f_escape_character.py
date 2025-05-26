txt = "We are the so-called \"Vikings\" from the north."
print(txt) # Output: We are the so-called "Vikings" from the north.

txt = 'It\'s alright.'
print(txt) # Output: It's alright.

txt = "This will insert one \\ (backslash)."
print(txt) # Output: This will insert one \ (backslash).

txt = "Hello\nWorld!"
print(txt) 
# Output:
# Hello 
# World!

txt = "Hello\rWorld!"
print(txt) # Output: World! (overwrites Hello)

txt = "Hello\tWorld!"
print(txt) # Output: Hello    World! (tab space)

# This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) # Output: HelloWorld! (removes the space)

# A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) # Output: Hello (octal values for H, e, l, l, o)

# A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) # Output: Hello (hex values for H, e, l, l, o)
