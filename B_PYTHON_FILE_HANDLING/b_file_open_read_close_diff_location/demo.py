# use r to treat the path as a raw string, where backslashes are interpreted literally.
# if r is not used, I'll get invalid escape sequence error

# It is a good practice to always close the file when you are done with it.
# Use the with statement to open the file, which will automatically close it for you.

filePath = r"E:\Git\w3schools_python\file_handling\b_file_open_read_close_diff_location\sub_folder\demo_file.txt"

with open(filePath) as f:
    print(f.read())