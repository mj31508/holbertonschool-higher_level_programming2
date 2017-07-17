-- script that creates the MYSQL server user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd'; --setting the pw and making sure the script doesnt fail
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost'; -- granting privileges to user
FLUSH PRIVILEGES;
