import psycopg2

class System:
    def __init__():
        pass
    
    @staticmethod
    def readFromDB(sql):
        conn=psycopg2.connect(host="localhost",dbname="python",user="postgres",password="admin")
        cursor=conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @staticmethod
    def writeToDB(sql):
        conn=psycopg2.connect(host="localhost",dbname="python",user="postgres",password="admin")
        cursor=conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()