from mysql import connector
from decouple import config

def create_db(DB_NAME):
    try:
        
        connection = connector.Connect(
            host=config('MYSQL_HOST'),
            user=config("MYSQL_USERNAME"),
            password=config("MYSQL_PASSWORD")
        )

        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS {} CHARACTER SET utf8 COLLATE utf8_general_ci;".format(DB_NAME))
        connection.close()
    except:
        raise ConnectionError
