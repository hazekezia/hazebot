import mysql.connector, os

def connecting_db():
    db = mysql.connector.connect(
        host=os.getenv("host"),
        user=os.getenv("user"),
        passwd=os.getenv("passwd"),
        database=os.getenv("database")
    )
    return db