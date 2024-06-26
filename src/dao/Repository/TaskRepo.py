import sqlite3

class TaskRepository:
    def __init__(self):
        self.cnx = sqlite3.connect('tasks.db')
        self.cursor = self.cnx.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tareas (
                Nombre TEXT,
                Descripcion TEXT,
                Fecha TEXT NOT NULL,
                Hora TEXT NOT NULL,
                PRIMARY KEY (Fecha, Hora)
            );
        """)

    def añadir_tarea(self, nombre, descripcion, fecha, hora):
        query = "INSERT INTO tareas (Nombre, Descripcion, Fecha, Hora) VALUES (?, ?, ?, ?)"
        valores = (nombre, descripcion, fecha, hora)
        try:
            self.cursor.execute(query, valores)
            self.cnx.commit()
            return 1
        except sqlite3.IntegrityError:
            return -1

    def eliminar_tarea(self, fecha, hora):
        query = "DELETE FROM tareas WHERE Fecha = ? AND Hora = ?"
        valores = (fecha, hora)
        self.cursor.execute(query, valores)
        self.cnx.commit()
    def editar_tarea(self, nombre, descripcion, fecha, hora):
        query = "UPDATE tareas SET Nombre = ?, Descripcion = ? WHERE Fecha = ? and Hora = ?"
        valores = (nombre,descripcion, fecha, hora)
        try:
            self.cursor.execute(query, valores)
            self.cnx.commit()
            return 1
        except sqlite3.IntegrityError:
            return -1
    
    def obtener_tareas(self):
        self.cursor.execute("SELECT * FROM tareas")
        return self.cursor.fetchall()
