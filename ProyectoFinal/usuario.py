import sqlite3


class Usuario:

    def __init__(self, nombre, apellido, contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.contraseña = contraseña

    def registrarUsuario(self):
        conexion = sqlite3.connect('database/usuarios.db')
        cursor = conexion.cursor()

        cursor.execute('INSERT INTO usuario (nombre, apellido, contraseña, tipo) VALUES (?,?,?,?)', (self.nombre,self.apellido,self.contraseña,'EMPLEADO'))
        conexion.commit()
        conexion.close()
