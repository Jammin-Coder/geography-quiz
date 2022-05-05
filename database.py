import mysql.connector
from settings import DB_HOST, DB_NAME, DB_PASSWORD, DB_USERNAME

def db_connect():
    return mysql.connector.connect(
        user=DB_USERNAME,
        password=DB_PASSWORD,
        host=DB_HOST,
        database=DB_NAME
    )