from datetime import datetime
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['python_quiz']
questions = list(mydb["questions"].find())
choices = list(mydb["choices"].find())
correctAnswersCtr = 0

print("""Welcome to the Python Quiz!
You will be asked a series of questions.
Please answer with the letter corresponding to your choice.
""")

name = input("Input your name: ")

user = mydb["users"].find_one({"username": name})
if user:
    deleteRecord = input(f"Welcome back, {name}! You have played this quiz before. Do you want to delete your previous record? (y/n): ")
    
    if deleteRecord == 'y':
        mydb["users"].delete_one({"username": name})
        print("Your previous record has been deleted.\n")

print("Hello " + name + "! Let's start the quiz.\n")

for x in questions:
    print(x["question"])
    
    questionChoices = [y for y in choices if y['question_id'] == x["_id"]]
    for choice in questionChoices:
        print(choice["choice"])
        
    answer = input("Answer: ")
    
    if answer == x["answer"]:
        correctAnswersCtr += 1
        
    print("\n")
    
print("You got " + str(correctAnswersCtr) + " out of " + str(len(questions)) + " correct.")

user = mydb["users"].find_one({"username": name})

if user:
    numTries = user.get("num_tries", 0) + 1
    mydb["users"].update_one({"username": name},
                             {"$set": {"correct_score": correctAnswersCtr, "num_tries": numTries, "last_played": datetime.now()}})
else:
    mydb["users"].insert_one({
        "username": name,
        "correct_score": correctAnswersCtr,
        "num_tries": 1,
        "last_played": datetime.now()
    })    