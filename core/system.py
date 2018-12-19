import psycopg2
import hashlib
import time

class System:
    def __init__(self):
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

    @staticmethod
    def generateId():
        return hashlib.sha256(str.encode(str(time.time()))).hexdigest()
