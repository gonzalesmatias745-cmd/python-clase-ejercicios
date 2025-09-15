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
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
cursor.execute("""
    INSERT INTO usuarios (nombre, apellido) VALUES (%s, %s)
""", (nombre, apellido))
conn.commit()
cursor.close()
conn.close()