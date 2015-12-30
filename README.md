# Python-CSV-to-SQL-Parser

This is a small script that enables you to be able to parse a csv file into a SQL database. It is capable of just inserting certain columns or all of the columns of the CSV file into a database. This is all done by editing the config.ini file. 

Currently, this relies on the database already having been created. There is also currently no way to be able to filter what rows are to be inserted into the database and therefore all rows will be parsed and inserted. Although, of course if your SQL is good enough you can filter the columns later. 

Also, error checking in this version is somewhat limited however, this is something that I am looking to develop in future iterations. Please report any issues that you find and let me know of any future improvements that you would like to see. 

Currently, the improvements look as follows: 
 - Improved error checking / handling 
 - Ability to create database as well as use existing ones 
 - Ability to be able to filter data post insertion
