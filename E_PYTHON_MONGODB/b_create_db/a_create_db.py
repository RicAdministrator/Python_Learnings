import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['mydatabase']

# database created!
# Important: In MongoDB, a database is not created until it gets content!
# MongoDB waits until you have created a collection (table), 
# with at least one document (record) before it actually creates the database (and collection).