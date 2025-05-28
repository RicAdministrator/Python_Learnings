USE w3schools_python

SELECT * FROM customers

CREATE TABLE products (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255))

CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))

CREATE TABLE products (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        FOREIGN KEY (id) REFERENCES users(id))

-------------
CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))


CREATE TABLE products (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255))

CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), product_id INT, FOREIGN KEY (product_id) REFERENCES products(id))

-----------------

INSERT INTO products
    (name)
VALUES
    ('Chocolate Heaven'),
    ('Tasty Lemons'),
    ('Vanilla Dreams')
    
INSERT INTO products(name) VALUES ('Chocolate Heaven'), ('Tasty Lemons'), ('Vanilla Dreams')    

---------------

SELECT * FROM users
SELECT * FROM products