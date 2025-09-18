-- SQL script to create users table and insert sample data
CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);


-- Create application user and grant privileges
CREATE USER IF NOT EXISTS 'testuser'@'%' IDENTIFIED BY 'testpass';
GRANT ALL PRIVILEGES ON demo.* TO 'testuser'@'%';
FLUSH PRIVILEGES;

INSERT INTO users (id, name) VALUES (1, 'Alice'), (2, 'Bob')
    ON DUPLICATE KEY UPDATE name=VALUES(name);
