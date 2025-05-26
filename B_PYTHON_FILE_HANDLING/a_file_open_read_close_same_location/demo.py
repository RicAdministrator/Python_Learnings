#  Opens a file and prints the content

# It is a good practice to always close the file when you are done with it.
# Use the with statement to open the file, which will automatically close it for you.

with open("demo_file.txt") as f:
    print(f.read())