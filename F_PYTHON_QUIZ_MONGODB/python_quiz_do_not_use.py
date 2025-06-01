from datetime import datetime
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['python_quiz']

correctAnswersCtr = 0

questionsAAA = list(mydb["questions"].find())
print(questionsAAA)

print("""Welcome to the Python Quiz!
You will be asked a series of questions.
Please answer with the letter corresponding to your choice.
""")

name = input("Input your name: ")

question_count = mydb["questions"].count_documents({})
user_count = mydb["users"].count_documents({ "username": name })

if user_count > 0:
    deleteRecord = input(f"Welcome back, {name}! You have played this quiz before. Do you want to delete your previous record? (y/n): ")
    
    if deleteRecord.lower() == 'y':
        mydb["users"].delete_one({ "username": name })
        print("Your previous record has been deleted.\n")
        
print("Hello " + name + "! Let's start the quiz.\n")

# ask each question
for x in mydb["questions"].find():
    # print question
    print(x.get("question"))
    
    # get choices for the question
    questionChoices = mydb["choices"].find({"question_id": x.get("_id")})
    
    # print choices
    for y in questionChoices:
        print(y.get("choice"))
    
    answer = input("Answer: ")
    
    if answer == x.get("answer"):
        correctAnswersCtr += 1
        
    print("\n")
    
print("You got " + str(correctAnswersCtr) + " out of " + str(question_count) + " correct.")   

# check if user exists in users table
# if user exists, update user's record
# if user does not exist, insert a new record   
user_count = mydb["users"].count_documents({ "username": name })   

# if user_count > 0:
#     mydb["users"].query({ "username": name }).get("num_tries")
    # numTries = 
    # mydb["users"].update_one({"username": name},
    #                          {"$set": {"correct_score": correctAnswersCtr, "date": datetime.now()}})