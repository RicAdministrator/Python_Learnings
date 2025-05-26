# if the file exists, delete it; if not, create it

import os

filePath = "demo_file.txt"

if os.path.exists(filePath):
    os.remove(filePath)
    print("The file has been deleted")
  
else:
    f = open(filePath, "x")
    print("The file has been created")