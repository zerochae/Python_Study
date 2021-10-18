import pymysql


class StockDao:

    def __init__(self):

        self.conn = pymysql.connect(
            user='root',
            password='python',
            host='127.0.0.1',
            database='python',
            port=3305
        )

        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

    def nameSelect(self):

        arr = []

        sql = "select DISTINCT s_name FROM stock "

        self.cur.execute(sql)

        result = self.cur.fetchall()

        for i in result:
            arr.append(i['s_name'])

        return arr

    def select(self, s_name):

        arr = []

        sql = f"""
        
            select price from stock where s_name = '{s_name}'
        """

        self.cur.execute(sql)

        result = self.cur.fetchall()

        for i in result:
            arr.append(i['price'])

        return arr

    def select100(self,s_name):

        arr = []

        sql = f"""
        
            select price from stock where s_name = '{s_name}'
        """

        self.cur.execute(sql)

        result = self.cur.fetchall()

        for i in result:
            arr.append(i['price'])

        value = arr[0]
        for i,j in enumerate(arr) :
            if arr[i] == 0 :
                arr[i] = 0.9999999
            else :
                arr[i] /= value

        return arr

    def insert(self, s_code, s_name, price, g_time):

        sql = """
        
            insert into stock(s_code,s_name,price,g_time)
            values (%s,%s,%s,%s)

        """

        cnt = self.cur.execute(sql, (s_code, s_name, price, g_time))
        return cnt

    def mycommit(self):

        self.conn.commit()

    def __del__(self):

        self.conn.close()
        self.cur.close()

    