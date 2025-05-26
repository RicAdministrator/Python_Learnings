# To create a new file in Python, use the open() method, with one of the following parameters:
# "x" - Create - will create a file, returns an error if the file exists
# "a" - Append - will create a file if the specified file does not exists
# "w" - Write - will create a file if the specified file does not exists

import datetime

strCurrentDateTime = str(datetime.datetime.now()).replace("-", "_").replace(" ", "_").replace(":", "_").replace(".", "_")
fileName = f"myfile_{strCurrentDateTime}.txt"

f = open(fileName, "x")