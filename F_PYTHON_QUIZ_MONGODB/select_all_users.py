import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["python_quiz"]
users = list(mydb["users"].find())

if users:
    print("Users found in the database:")   
    for x in users:
        print(x)
else:
    print("No users found in the database.")