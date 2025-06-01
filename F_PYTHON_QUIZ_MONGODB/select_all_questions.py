import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["python_quiz"]
mycol = mydb["questions"]

for x in mycol.find():
  print(x)