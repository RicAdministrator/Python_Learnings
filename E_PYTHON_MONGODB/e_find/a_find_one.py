# In MongoDB we use the find() and find_one() methods to find data in a collection.
# Just like the SELECT statement is used to find data in a table in a MySQL database.

# Find One
# To select data from a collection in MongoDB, we can use the find_one() method.
# The find_one() method returns the first occurrence in the selection.

# Find the first document in the customers collection:
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

x = mycol.find_one()

print(x)