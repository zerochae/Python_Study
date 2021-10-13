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