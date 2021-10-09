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
    update emp
    set emp_name = '6', tel ='6', address='6'
    where emp_id='5'
"""

cnt = cur.execute(sql)

print(cnt)
mydb.commit()
cur.close()
mydb.close()