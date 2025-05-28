import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)

mycursor = mydb.cursor()

# drop create db
mycursor.execute("DROP DATABASE IF EXISTS python_quiz")
mycursor.execute("CREATE DATABASE python_quiz")

# update mydb and mycursor to use python_quiz db
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="python_quiz"
)

mycursor = mydb.cursor()

# create tables
mycursor.execute("CREATE TABLE questions (id INT AUTO_INCREMENT PRIMARY KEY, question VARCHAR(255), answer VARCHAR(1))")
mycursor.execute("CREATE TABLE choices (id INT AUTO_INCREMENT PRIMARY KEY, choice VARCHAR(255), question_id INT, FOREIGN KEY (question_id) REFERENCES questions(id))")
mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), correct_score INT, num_tries INT,last_played TIMESTAMP)")

# create questions data 
mycursor.execute("""
INSERT INTO questions(question, answer) VALUES 
('What is the correct file extension for Python files?', 'c'), 
('What is a correct command line syntax for checking if python is installed on your computer? (And also to check the Python version)', 'a'), 
('What is a correct syntax to exit the Python command line interface?', 'a'),
('True or False: Indentation in Python is for readability only.', 'b')
""")
mydb.commit()

# create choices data 
mycursor.execute("""
INSERT INTO choices(choice, question_id) VALUES 
('a) .pp', 1), 
('b) .pt', 1), 
('c) .py', 1),

('a) python --version', 2), 
('b) python ##version', 2), 
('c) python version', 2),

('a) exit()', 3), 
('b) stop()', 3), 
('c) end()', 3),

('a) True', 4), 
('b) False', 4)
""")
mydb.commit()