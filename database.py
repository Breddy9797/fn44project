import psycopg2
from load import DB_NAME, DB_USER, DB_PASS, DB_HOST, DB_PORT

def connection():
    return psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT,
    )

connection().autocommit = True

def jadval_yaratish():
    conn = connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255),
    telegrm_id VARCHAR(255)
    )
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("Jadval yaratildi!")

def malumot(toliqismi, telegrm_ids):
    conn = connection()
    cur = conn.cursor()
    cur.execute("""INSERT INTO users (full_name, telegrm_id) VALUES (%s, %s);""",(toliqismi, telegrm_ids))
    conn.commit()
    cur.close()
    conn.close()


