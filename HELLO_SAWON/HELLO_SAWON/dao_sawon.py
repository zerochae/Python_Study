import pymysql

class SawonDao :

    def __init__(self) :

        self.conn = pymysql.connect(
            user = 'root',
            password = 'python',
            host = '127.0.0.1',
            database = 'python',
            port = 3305
        )
 
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

    
    def myselect(self) :

        self.cur.execute("select * from sawon")
        result = self.cur.fetchall()

        return result

    def myinsert(self,s_name,s_mobile,dept_name) :

        sql = f"""
        
            insert into sawon(s_name,s_mobile,dept_name)
            values ({s_name},{s_mobile},{dept_name})
        
        """

        cnt = self.cur.execute(sql)
        self.conn.commit()
        return cnt

    def myupdate(self,s_id,s_name,s_mobile,dept_name) :

        sql = f"""
        
            update sawon
            set s_name = '{s_name}', s_mobile= '{s_mobile}', dept_name = '{dept_name}'
            where s_id = '{s_id}'
        """

        cnt = self.cur.execute(sql)
        self.conn.commit()
        return cnt

    def mydelete(self,s_id) :

        sql = f"""
        
            delete from sawon
            where s_id = "{s_id}"
        
        """

        cnt = self.cur.execute(sql)
        self.conn.commit()
        return cnt

    def __del__(self) :
        self.conn.close()
        self.cur.close()    