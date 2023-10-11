import psycopg2
from settings import *

class DBPostgres():
    def __init__(self):
        self.conn = psycopg2.connect(
                    dbname = DB_NAME,
                    user = DB_USER,
                    host = DB_HOST, 
                    password = DB_PASSWORD,
                    port = DB_PORT
                    )
        self.cursor  = self.conn.cursor() 

    def get_execute(self, request:str, param:tuple):
            try:
                self.cursor.execute(request, param)
                self.conn.commit()
                return True
            except:
                self.conn.rollback()
                return False

    def set_record(self, values:tuple):
            request = f'''
                    INSERT INTO "{TABLE_NAME}" 
                    ({ID_QUESTION}, {ANSWER}, {QUESTION}, {CREATED}) 
                    values (%s, %s, %s, %s)'''
            return self.get_execute(request, values)