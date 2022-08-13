
import config
from mysql.connector import connect, Error


def db_created_table_art(message):
    try:
        with connect(
                host=config.db_conf["host"],
                user=config.db_conf["user"],
                password=config.db_conf["password"],
        ) as connection:
            show_db_query = "SHOW DATABASES"
            with connection.cursor() as cursor:
                cursor.execute(show_db_query)
                for db in cursor:
                    print(db)
    except Error as e:
        print(e)