import pymysql
from pymysql.err import error_map


class StockDao2:

    def __init__(self):

        self.conn = pymysql.connect(
            user='root',
            password='python',
            host='127.0.0.1',
            database='_stock_old',
            port=3305
        )

        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

    def selectName(self):

        arr = []

        sql = """

        SELECT `COLUMN_NAME`
        FROM `INFORMATION_SCHEMA`.`COLUMNS`
        WHERE `TABLE_SCHEMA`='_stock_old'
        AND `TABLE_NAME`='stock_sync_0121';

        """

        self.cur.execute(sql)

        result = self.cur.fetchall()

        for i in result:
            arr.append(i['COLUMN_NAME'])

        return arr

    def selectPrice(self, name):

        arr = []

        sql = f"""

        SELECT {name} FROM stock_sync_0121

        """

        self.cur.execute(sql)

        result = self.cur.fetchall()

        for i in result:
            arr.append(i[name])

        for j in arr:
            # if arr[0] == 0:
            #     j = 0.98
            # else:
            j /= arr[0]

        return arr

    def myselect100(self, name):

        priceArr = []
        sql = f"""
                select {name} from stock_sync_0121
            """
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        for i in rows:
            priceArr.append(i[name])
            
        returnArr = []
        for i,j in enumerate(priceArr):
            
            if i == len(priceArr)-1 : break
            
            if priceArr[0] == 0:
                returnArr.append(0.98)
            else:
                returnArr.append(j / priceArr[0])
        return returnArr   
