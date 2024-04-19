import sqlite3


class Cliente:

    def __init__(self, tipodoc, numdoc, fecexpdoc, nombre, apellido1, apellido2, pais, fecnac, habitacion):
        self.tipodoc = tipodoc
        self.numdoc = numdoc
        self.fecexpdoc = fecexpdoc
        self.nombre = nombre
        self.apellido1 = apellido1
        if apellido2 != "":
            self.apellido2 = apellido2
        else:
            self.apellido2 = ""
        self.pais = pais
        self.fecnac = fecnac
        self.habitacion = habitacion



    def registrarCliente(self):
        conexion = sqlite3.connect('database/usuarios.db')
        cursor = conexion.cursor()

        cursor.execute('INSERT INTO clientesTEMP VALUES (?,?,?,?,?,?,?,?,?)', (self.tipodoc,self.numdoc,self.fecexpdoc,self.nombre,self.apellido1,self.apellido2,self.fecnac,self.pais,self.habitacion))
        conexion.commit()
        conexion.close()
