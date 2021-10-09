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
        insert into emp (emp_id, emp_name, tel, address) 
               values (%s,%s,%s,%s)
      """
val = ("5","5","5","5")

cur.execute(sql,val)
mydb.commit()

print(cur.rowcount, "line insert success")

cur.close()
mydb.close()