import psycopg2


def db_connection():
    """ function to open connection """
    conn = psycopg2.connect(
        host='localhost',
        port=5432,
        database='data_blog_complete',
        user='postgres',
        password='mahesa889'
    )
    return conn
