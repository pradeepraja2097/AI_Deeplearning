import sqlite3

connection=sqlite3.connect("/home/pradeep/Documents/Deeplearning/sqlite/test.db")
select_operation=connection.cursor()
select_operation.execute("select Distinct(Grade) from student")
ans=select_operation.fetchall()

for i in ans:
    print(i)
print("hello")


