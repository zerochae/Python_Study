import pymysql

class MovieDao :
    
    def __init__(self) :

        self.conn = pymysql.connect(

            user = 'root',
            password = 'python',
            host = '127.0.0.1',
            database= 'python',
            port = 3305

        )

        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

    def myInsert(self,title,link,image,subtitle,pubData,director,actor,userRating) :

        # sql = f"""

        #     insert into movie (title,link,image,subtitle,pubData,director,actor,userRating)
        #     values ({title},{link},{image},{subtitle},{pubData},{director},{actor},{userRating})

        # """

        sql = """
        
        insert into movie (title,link,image,subtitle,pubData,director,actor,userRating)
            values (%s,%s,%s,%s,%s,%s,%s,%s)
        
        """

        cnt = self.cur.execute(sql,(title,link,image,subtitle,pubData,director,actor,userRating))
        self.conn.commit()
        return cnt

        