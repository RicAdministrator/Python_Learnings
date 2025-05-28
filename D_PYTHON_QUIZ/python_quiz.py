import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="python_quiz"
)

mycursor = mydb.cursor()

# get questions from questions table
mycursor.execute("SELECT * FROM questions")
questions = mycursor.fetchall()

# get choices from questions table
mycursor.execute("SELECT * FROM choices")
choices = mycursor.fetchall()

correctAnswersCtr = 0

print("""Welcome to the Python Quiz!
You will be asked a series of questions.
Please answer with the letter corresponding to your choice.
""")

name = input("Input your name: ")

mycursor.execute("SELECT * FROM users WHERE username = %s", (name,))
user = mycursor.fetchall()

if len(user) > 0:
    deleteRecord = input(f"Welcome back, {name}! You have played this quiz before. Do you want to delete your previous record? (y/n): ")

    if deleteRecord == 'y':
        mycursor.execute("DELETE FROM users WHERE username = %s", (name,))
        mydb.commit()
        print("Your previous record has been deleted.\n")

print("Hello " + name + "! Let's start the quiz.\n")

# ask each question
for x in questions:
    # print question
    print(x[1])
    
    # get choices for the question
    questionChoices = [i for i in choices if i[2] == x[0]]
    
    # print choices
    for y in questionChoices:
        print(y[1])
    
    answer = input("Answer: ")
    
    if answer == x[2]:
        correctAnswersCtr += 1
        
    print("\n")
    
print("You got " + str(correctAnswersCtr) + " out of " + str(len(questions)) + " correct.")

# check if user exists in users table
# if user exists, update user's record
# if user does not exist, insert a new record
mycursor.execute("SELECT * FROM users WHERE username = %s", (name,))
user = mycursor.fetchall()

if len(user) > 0:
    numTries = user[0][3] + 1
    mycursor.execute("UPDATE users SET correct_score = %s, num_tries = %s, last_played = NOW() WHERE username = %s", (correctAnswersCtr, numTries, name))
else:
    mycursor.execute("INSERT INTO users (username, correct_score, num_tries, last_played) VALUES (%s, %s, 1, NOW())", (name, correctAnswersCtr))

mydb.commit()