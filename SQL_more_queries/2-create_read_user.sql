-- Creates database hbtn_0d_2 and user user_0d_2
-- Database creation
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- User creation with password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Granting only SELECT privilege on the specific database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
-- Apply changes
FLUSH PRIVILEGES;
