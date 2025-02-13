import psycopg2

def get_db_connection():
    
    conn = psycopg2.connect(database="NewDB", 
                            host="localhost", 
                            user="postgres",
                            password="admin", 
                            port="5432")
    return conn
