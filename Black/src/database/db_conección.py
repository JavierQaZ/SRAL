from decouple import config
import pymysql

def get_connection():
    try:
        #devuelve una conexion (socket)
        return pymysql.connect( 
            host = config('MYSQL_HOST'),
            user = config('MYSQL_USER'),
            password = config('MYSQL_PASSWORD'),
            db = config('MYSQL_DB')
        )
    except Exception as exc:
        print(exc)