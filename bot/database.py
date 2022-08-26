import mysql.connector, os

from dotenv import load_dotenv
load_dotenv()

def connecting_db():
    db = mysql.connector.connect(
        host=os.getenv("host"),
        user=os.getenv("user"),
        passwd=os.getenv("passwd"),
        database=os.getenv("database")
    )
    return db