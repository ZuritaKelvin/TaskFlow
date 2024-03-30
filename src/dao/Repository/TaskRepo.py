import mysql.connector

class TaskRepository:
    def __init__(self):
        self.cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root"
        )
        self.cursor = self.cnx.cursor()
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS Task")
        self.cursor.execute("USE Task")
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tareas (
                Nombre VARCHAR(255),
                Descripcion VARCHAR(255),
                Fecha DATE,
                Hora TIME,
                UNIQUE (Fecha, Hora)
            );
        """)

    def añadir_tarea(self, nombre, descripcion, fecha, hora):
        tareas = self.obtener_tareas()
        query = "INSERT INTO tareas (Nombre, Descripcion, Fecha, Hora) VALUES (%s, %s, %s, %s)"
        valores = (nombre, descripcion, fecha, hora)
        try:
            self.cursor.execute(query, valores)
            self.cnx.commit()
            return 1
        except:
            return -1

    def eliminar_tarea(self, nombre):
        query = "DELETE FROM tareas WHERE Nombre = %s"
        valores = (nombre,)
        self.cursor.execute(query, valores)
        self.cnx.commit()

    def editar_tarea(self, nombre, descripcion, fecha, hora):
        query = "UPDATE tareas SET Descripcion = %s, Fecha = %s, Hora = %s WHERE Nombre = %s"
        valores = (descripcion, fecha, hora, nombre)
        try:
            self.cursor.execute(query, valores)
            self.cnx.commit()
            return 1
        except:
            return -1
    
    def obtener_tareas(self):
        self.cursor.execute("SELECT * FROM tareas")
        return self.cursor.fetchall()