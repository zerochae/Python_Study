import pymysql

class DaoMember :

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

        sql = """
            select m_id,m_name,mobile,up_date,in_date 
            from member
        """

        self.cur.execute(sql)
        result = self.cur.fetchall()

        return result
    
    def myinsert(self,m_id,m_name,mobile) :

        sql = f"""
                insert into member (m_id,m_name,mobile,up_date,in_date)
                values ('{m_id}','{m_name}','{mobile}',DATE_FORMAT(now(), "%Y%m%d"),DATE_FORMAT(now(), "%Y%m%d"))
        """
    
        cnt = self.cur.execute(sql)
        self.conn.commit()

        return cnt

    def myupdate(self,m_id,m_name,mobile,up_date,in_date) :

        sql = f"""
                update member
                set m_name = "{m_name}", mobile = "{mobile}" , up_date = "{up_date}", in_date = "{in_date}"
                where m_id = "{m_id}" 
        """

        cnt = self.cur.execute(sql)
        self.conn.commit()
        return cnt
    
    def mydelete(self,m_id) :

        sql = f"""
                delete from member
                where m_id = '{m_id}'
        """
        cnt = self.cur.execute(sql)
        self.conn.commit()
        return cnt
    
    def __del__(self) :
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':

    daoMember = DaoMember()

    cnt = daoMember.myinsert("02","권주현","119")
    # cnt = daoMember.myselect()
    print(cnt)
    
