# Open the file "demo_file.txt" and append content to the file
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

import datetime

with open("demo_file.txt", "a") as f:
  f.write("\n" + "This line was added on " + str(datetime.datetime.now()))

#open and read the file after the appending:
with open("demo_file.txt") as f:
  print(f.read())