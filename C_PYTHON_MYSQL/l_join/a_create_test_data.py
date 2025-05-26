import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="w3schools_python"
)

mycursor = mydb.cursor()

# Drop tables if it exists to start fresh
mycursor.execute("DROP TABLE IF EXISTS users")
mycursor.execute("DROP TABLE IF EXISTS products")

# Create products table
mycursor.execute("CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")

# Create users table
mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), product_id INT, FOREIGN KEY (product_id) REFERENCES products(id))")

# Insert test data into products table
mycursor.execute("INSERT INTO products(name) VALUES ('Chocolate Heaven'), ('Tasty Lemons'), ('Vanilla Dreams')")
mydb.commit()

# Insert test data into users table
sql = "INSERT INTO users (name, product_id) VALUES (%s, %s)"
val = [
  ('John', 1),
  ('Peter', 1),
  ('Amy', 2),
  ('Hannah', None),
  ('Michael', None)
]
mycursor.executemany(sql, val)
mydb.commit()

