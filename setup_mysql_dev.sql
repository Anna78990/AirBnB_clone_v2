-- This script will create the database --
-- hbnb_dev_db should have all privileges on hbnb_dev_db and SELECT on performance schema --
CREATE DATABASE IF NOT EXISTS 'hbnb_dev_db';
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT * ON 'hbnb_dev_db' TO 'hbnb_dev'@'localhost';
GRANT SELECT ON 'performance_schema' TO 'hbnb_dev'@'localhost';
