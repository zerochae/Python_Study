import pymysql

mydb = pymysql.connect(
    user='root', 
    password='python',
    host='127.0.0.1',
    database='python',
    port = 3305
    )

cur = mydb.cursor()

cur.execute("select * from emp")

myresult = cur.fetchall()

for i in myresult :
    print(i)
 
cur.close()
mydb.close()