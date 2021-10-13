import pymysql

class DaoEmp :

    def __init__(self) :

        self.conn = pymysql.connect(
            user = 'root',
            password = 'python',
            host = '127.0.0.1',
            database = 'python',
            port = 3305
        )

        self.cur = self.conn.cursor()

    def myselect(self) :

        self.cur.execute("select * from emp")
        result = self.cur.fetchall()

        return result

    def myinsert(self,emp_id,emp_name,tel,address) :

        sql = f"""
        insert into emp (emp_id, emp_name, tel, address) 
               values ("{emp_id}","{emp_name}","{tel}","{address}")
        """

        cnt = self.cur.execute(sql)
        self.conn.commit()
        return cnt

    def myupdate(self,emp_id,emp_name,tel,address) :

        sql = f"""
                update emp
                set emp_name = "{emp_name}", tel = "{tel}" , address = "{address}"
                where emp_id = "{emp_id}" 
        """

        cnt = self.cur.execute(sql)
        self.conn.commit()
        return cnt

    def mydelete(self,emp_id) :

        sql = f"""
                delete from emp
                where emp_id = "{emp_id}"
        """

        cnt = self.cur.execute(sql)
        self.conn.commit()
        return cnt

    def __del__(self):
        self.conn.close()
        self.cur.close()

if __name__ == '__main__':
    de = DaoEmp()
    # lst = de.myselect()
    # print(lst)

    # cnt = de.myinsert("5","5","5","5")
    cnt = de.myupdate("5","6","6","6")
    print(cnt)