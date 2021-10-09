import pymysql

mydb = pymysql.connect(
    user='root', 
    password='python',
    host='127.0.0.1',
    database='python',
    port = 3305
    )

cur = mydb.cursor()

sql = """
        delete from emp where emp_id=%s
"""

val = "5"

cnt = cur.execute(sql,val)

print(cnt)

mydb.commit()

cur.close()
mydb.close()