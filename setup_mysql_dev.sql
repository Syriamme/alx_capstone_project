-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS expense_db;
CREATE USER IF NOT EXISTS 'Daniel'@'localhost' IDENTIFIED BY 'new_password';
GRANT ALL PRIVILEGES ON `expense_db`.* TO 'Daniel'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'Daniel'@'localhost';
FLUSH PRIVILEGES;
