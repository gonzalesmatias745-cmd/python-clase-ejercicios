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
cursor.execute("""
    INSERT INTO usuarios (nombre, apellido) VALUES
    ('Carlos', 'Ramírez'),
    ('Ana', 'Gómez'),
    ('Luis', 'Martínez'),
    ('María', 'Fernández'),
    ('Pedro', 'Sánchez'),
    ('Laura', 'Torres'),
    ('Jorge', 'Castro'),
    ('Camila', 'Suárez'),
    ('Andrés', 'Morales'),
    ('Valentina', 'Ortiz');
""")
conn.commit()
cursor.close()
conn.close()