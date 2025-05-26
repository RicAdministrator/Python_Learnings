# "w" - Write - will overwrite any existing content

import datetime

with open("demo_file.txt", "w") as f:
  f.write(f"Woops! I have deleted the content!\nOverwrite Date : {str(datetime.datetime.now())}")

#open and read the file after the overwriting:
with open("demo_file.txt") as f:
  print(f.read())