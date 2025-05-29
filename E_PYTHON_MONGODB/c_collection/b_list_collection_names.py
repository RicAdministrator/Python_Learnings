# Remember: In MongoDB, a collection is not created until it gets content

# You can check if a collection exist in a database by listing all collections:

# Return a list of all collections in your database:
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['mydatabase']

mycol = mydb["customers"]

print(mydb.list_collection_names())