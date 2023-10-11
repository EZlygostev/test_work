import psycopg2
from settings import *

request = f'''
CREATE TABLE "{TABLE_NAME}" (
{ID_RECORD} serial PRIMARY KEY,
{ID_QUESTION} integer NOT NULL,
{ANSWER} character varying(100) NOT NULL,
{QUESTION} character varying(100) NOT NULL,
{CREATED} character varying(100) NOT NULL,
UNIQUE({ID_QUESTION})
);'''

try:
    conn = psycopg2.connect(
            dbname = DB_NAME,
            user = DB_USER,
            host = DB_HOST, 
            password = DB_PASSWORD,
            port = DB_PORT
            )
    cursor  = conn.cursor() 
    cursor.execute(request)
    conn.commit()
    print("TABLE CREATE")
except Exception as ex:
	print ("ERROR CONNECTION ", ex)
