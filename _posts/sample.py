import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="fhrtmxk7517~",
    database="python_db"
)

cursor = conn.cursor()

cursor.execute("DELETE FROM users WHERE id =1")
conn.commit()


cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

cursor.close()
conn.close()