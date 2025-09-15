import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="trabajo",
    user="postgres",
    password="1234",
    port=5433
)
print(conn)
print("Conexión exitosa a la base de datos")
cursor = conn.cursor()
cursor.execute("CREATE TABLE usuarios(id SERIAL PRIMARY KEY, nombre VARCHAR(100), apellido VARCHAR(100))")
conn.commit()
cursor.close()
conn.close()