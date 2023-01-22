import sqlite3  # module for python

#Establishing connection
connection=sqlite3.connect("/home/pradeep/Documents/Deeplearning/sqlite/test.db") #It will check try to connect with exisiting or reat new

cursor=connection.cursor() #It will create connection and move the cursor inside DB

#delete
cursor.execute('''Drop Table Student;''')


#creating table

sql_command=""" CREATE TABLE Student(
    RollNo INTEGER PRIMARY KEY,
    Sname VARCHAR (20),
    Grade CHAR(1),
    gender CHAR(1),
    Avg DECIMAL (5,2),
    birth_date DATE);"""

# cursor.execute(sql_command)

sql_command=""" INSERT INTO
                Student(RollNo,Sname,Grade,gender,Avg,birth_date)
                VALUES(null,Pradeep,'A','M',"87.3","20.06.1997");"""
cursor.execute(sql_command)

connection.commit()
print("DB success")
