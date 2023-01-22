import sqlite3

connection=sqlite3.connect("/home/pradeep/Documents/Deeplearning/sqlite/test.db")
cursor=connection.cursor()

student_data=[("thiru","C","M","80","13.11.2022"),
("thiru1","B","M","80","14.11.2022"),
("thiru2","A","M","80","15.11.2022"),
("thiru3","D","M","80","16.11.2022"),]


for p in student_data:
    format_str=""" INSERT INTO Student(RollNo,Sname,Grade,gender,Avg,birth_date)

    VALUES(NULL,"{name}","{gr}","{gender}","{avg}","{birth_date}");"""


    sql_command=format_str.format(name=p[0],gr=p[1],gender=p[2],avg=p[3],birth_date=p[4])
    cursor.execute(sql_command)

connection.commit()
connection.close()