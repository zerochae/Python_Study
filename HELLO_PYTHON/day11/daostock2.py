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

        for i in result :
            arr.append(i['COLUMN_NAME'])

        return arr
    
    def selectPrice(self,name) :

        arr = []

        sql = f"""
        
        SELECT {name} FROM stock_sync_0121

        """

        self.cur.execute(sql)

        result = self.cur.fetchall()

        for i in result :
            arr.append(i[name])
        
        value = arr[0]

        for i,j in enumerate(arr) :
            if arr[i] == 0 :
                arr[i] = 0.99999999
            else :
                arr[i] /= value

        return arr

if __name__ == '__main__':
    sd = StockDao2()

    lst = sd.selectName()

    lst2 = sd.selectPrice('s000020')

    print(lst2)
    
