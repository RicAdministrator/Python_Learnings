from datetime import datetime
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['python_quiz']

# drop db
myclient.drop_database(mydb)

# create questions table and insert records
questions_table = mydb["questions"]
questions = [
  { "_id": 1, "question": "What is the correct file extension for Python files?", "answer": "c"},
  { "_id": 2, "question": "What is a correct command line syntax for checking if python is installed on your computer? (And also to check the Python version)", "answer": "a"},
  { "_id": 3, "question": "What is a correct syntax to exit the Python command line interface?", "answer": "a"},
  { "_id": 4, "question": "True or False: Indentation in Python is for readability only.", "answer": "b"}
]
questions_table.insert_many(questions)

# create choices table and insert records
choices_table = mydb["choices"]
choices = [
  { "choice": "a) .pp", "question_id": 1},
  { "choice": "b) .pt", "question_id": 1},
  { "choice": "c) .py", "question_id": 1},
  
  { "choice": "a) python --version", "question_id": 2},
  { "choice": "b) python ##version", "question_id": 2},
  { "choice": "c) python version", "question_id": 2},
  
  { "choice": "a) exit()", "question_id": 3},
  { "choice": "b) stop()", "question_id": 3},
  { "choice": "c) end()", "question_id": 3},
  
  { "choice": "a) True", "question_id": 4},
  { "choice": "b) False", "question_id": 4}
]
choices_table.insert_many(choices)

# create users table and insert records
users_table = mydb["users"]
users = [
  { "username": "dummy user", "correct_score": 4, "num_tries": 1, "last_played": datetime.now() },
]
users_table.insert_many(users)

for x in questions_table.find():
  print(x)
    
print("-----")

for x in choices_table.find():
  print(x)
  
print("-----")

for x in users_table.find():
  print(x)



