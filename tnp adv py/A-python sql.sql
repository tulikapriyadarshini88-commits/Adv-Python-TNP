create database gietu;
use gietu;
CREATE TABLE student (
    roll INT PRIMARY KEY,
    name VARCHAR(50),
    rgdno int,
    dept varchar(10),
    salary int
);
INSERT INTO student VALUES (1, 'Ram', 101,'CSE', 100000);
INSERT INTO student VALUES (2, 'Radha', 102,'CSE', 100000);
INSERT INTO student VALUES (3, 'Khusi', 103,'CSE', 200050);
INSERT INTO student VALUES (4, 'Smriti', 103,'CSE', 100000);
INSERT INTO student VALUES (5, 'Kritika', 104,'CSE', 100000);
INSERT INTO student VALUES (6, 'Monika', 105,'CSE', 100000);
INSERT INTO student VALUES (7, 'Ram', 106,'ECE', 100000);
INSERT INTO student VALUES (8, 'Ram', 107,'CSE', 100000);
INSERT INTO student VALUES (9, 'Madhuri', 108,'CSE', 150000);
INSERT INTO student VALUES (10, 'Samarth', 109,'CSE', 160000);
Select * from student;