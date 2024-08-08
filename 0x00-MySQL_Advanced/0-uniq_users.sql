-- 0-uniq_users.sql
-- This script creates the users table with unique email addresses

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    PRIMARY KEY (id)
);

