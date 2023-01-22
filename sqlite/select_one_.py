import sqlite3

connection=sqlite3.connect("/home/pradeep/Documents/Deeplearning/sqlite/test.db")
select_operation=connection.cursor()
select_operation.execute("select* from student")
ans=select_operation.fetchone()

print(ans)

while ans is not None:
    print(ans)
    ans=select_operation.fetchone()
