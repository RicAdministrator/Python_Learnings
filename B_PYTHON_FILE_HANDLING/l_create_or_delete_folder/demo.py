# To delete an entire folder, use the os.rmdir() method
# You can only remove empty folders

import os

folderPath = "my_folder"

if not os.path.exists(folderPath):
    os.makedirs(folderPath)
    print("The folder has been created")

else:    
    os.rmdir(folderPath)
    print("The folder has been deleted")