import mysql.connector

# Conexión a MySQL
cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456'
)

cursor = cnx.cursor()

# Crear base de datos si no existe
cursor.execute("CREATE DATABASE IF NOT EXISTS Taks")

# Seleccionar la base de datos
cursor.execute("USE Taks")

# Crear tabla si no existe
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tareas (
        Nombre VARCHAR(80),
        Descripcion VARCHAR(200),
        Fecha DATE,
        Hora TIME
    )
""")

cnx.close()
