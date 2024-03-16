import mysql.connector

class Task:
    def __init__(self, host, usuario, contraseña):
        self.cnx = mysql.connector.connect(
            host=host,
            user=usuario,
            password=contraseña
        )
        self.cursor = self.cnx.cursor()
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS Task")
        self.cursor.execute("USE Task")
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tareas (
                Nombre VARCHAR(255),
                Descripcion VARCHAR(255),
                Fecha DATE,
                Hora TIME
            )
        """)

    def añadir_tarea(self, nombre, descripcion, fecha, hora):
        tareas = self.obtener_tareas()
        if tareas is not None:
            for i in tareas:
                if i[0] == nombre:return -1
        query = "INSERT INTO tareas (Nombre, Descripcion, Fecha, Hora) VALUES (%s, %s, %s, %s)"
        valores = (nombre, descripcion, fecha, hora)
        self.cursor.execute(query, valores)
        self.cnx.commit()
        return 1

    def eliminar_tarea(self, nombre):
        query = "DELETE FROM tareas WHERE Nombre = %s"
        valores = (nombre,)
        self.cursor.execute(query, valores)
        self.cnx.commit()

    def editar_tarea(self, nombre, descripcion, fecha, hora):
        tareas = self.obtener_tareas()
        for i in tareas:
            if i[0] == nombre:return -1
        query = "UPDATE tareas SET Descripcion = %s, Fecha = %s, Hora = %s WHERE Nombre = %s"
        valores = (descripcion, fecha, hora, nombre)
        self.cursor.execute(query, valores)
        self.cnx.commit()

    def obtener_tareas(self):
        self.cursor.execute("SELECT * FROM tareas")
        return self.cursor.fetchall()
    
# taskClass = Task('localhost','root','123456')
# # taskClass.añadir_tarea('Jugar','Debes jugar 30min de LOL','2024-03-12','10:30:00')
# taskClass.eliminar_tarea('Jugar')
# tareas = taskClass.obtener_tareas()
# for i in tareas:
#     print(i[3])