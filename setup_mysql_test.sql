-- This script will create the database (this is the test) --
-- hbnb_dev_db should have all privileges on hbnb_dev_db and SELECT on performance schema --
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER
	IF NOT EXISTS 'hbnb_test'@'localhost'
	IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL
	ON `hbnb_test_db`.*
	TO 'hbnb_test'@'localhost';
GRANT SELECT 
	ON `performance_schema`.*
	TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
