# Advanced Query
# To make advanced queries you can use modifiers as values in the query object.
# E.g. to find the documents where the "address" field starts with the letter "S" or higher (alphabetically), 
# use the greater than modifier: {"$gt": "S"}:

# Find documents where the address starts with the letter "S" or higher:
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

#address greater than S:
myquery = { "address": {"$gt": "S"} }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)