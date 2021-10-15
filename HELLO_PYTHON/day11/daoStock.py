import pymysql

class StockDao :

    def __init__(self) :

        self.conn = pymysql.connect(
            user = 'root',
            password= 'python',
            host = '127.0.0.1',
            database= 'python',
            port = 3305
        )

        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

    def insert(self,s_name,s_code,price,g_time) :

        sql ="""
        
            insert into stock(s_code,s_name,price,g_time)
            values (%s,%s,%s,%s)

        """

        cnt = self.cur.execute(sql,(s_code,s_name,price,g_time))
        return cnt

    def mycommit(self) :

        self.conn.commit()

    def __del__(self) :

        self.conn.close()
        self.cur.close()
    

