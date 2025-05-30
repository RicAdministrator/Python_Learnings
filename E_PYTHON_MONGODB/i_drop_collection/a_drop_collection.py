# Drop Collection
# You can drop a table, or collection as it is called in MongoDB, by using the drop() method.

# Drop the "customers" collection:
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mycol.drop()

# The drop() method returns true if the collection was dropped successfully, and false if the collection does not exist.