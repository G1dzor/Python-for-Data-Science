CREATE DATABASE IF NOT EXISTS my_database;

USE my_database;

CREATE TABLE IF NOT EXISTS titanic (
    id INT AUTO_INCREMENT PRIMARY KEY,
    PassengerId VARCHAR(255),
    Survived VARCHAR(255),
    Pclass  VARCHAR(255),
    Name VARCHAR(255),
    Sex VARCHAR(255),
    Age VARCHAR(255),
    SibSp VARCHAR(255),
    Parch VARCHAR(255),
    Ticket VARCHAR(255),
    Fare VARCHAR(255),
    Cabin VARCHAR(255),
    Embarked VARCHAR(255)
);

LOAD DATA INFILE '/var/lib/mysql-files/titanic.csv'
     INTO TABLE titanic
     FIELDS TERMINATED BY ","
     ENCLOSED BY '"'
     LINES TERMINATED BY '\n'
     IGNORE 1 ROWS
     (PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked);
