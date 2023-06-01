-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS dogplug_dev_db;

CREATE USER IF NOT EXISTS 'dogplug_dev'@'localhost' IDENTIFIED BY 'dogplug_dev_pwd';

GRANT ALL PRIVILEGES ON dogplug_dev_db.* TO 'dogplug_dev'@'localhost';

GRANT SELECT ON performance_schema.* TO 'dogplug_dev'@'localhost';

FLUSH PRIVILEGES;
