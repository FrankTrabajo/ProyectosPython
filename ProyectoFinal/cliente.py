import sqlite3


class Cliente:

    def __init__(self, tipodoc, numdoc, fecexpdoc, nombre, apellido1, apellido2, pais, fecnac, habitacion, fecEnt, fecSal):
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
        self.fecent = fecEnt
        self.fecsal = fecSal



    def registrarCliente(self):
        conexion = sqlite3.connect('database/usuarios.db')
        cursor = conexion.cursor()

        try:
            cursor.execute('INSERT INTO clientesTEMP VALUES (?,?,?,?,?,?,?,?,?,?,?)', (self.tipodoc,self.numdoc,self.fecexpdoc,self.nombre,self.apellido1,self.apellido2,self.fecnac,self.pais,self.habitacion, self.fecent, self.fecsal))
            cursor.execute('INSERT INTO clientesPER VALUES (?,?,?,?,?,?,?,?,?)', (self.tipodoc,self.numdoc,self.nombre,self.apellido1,self.apellido2,self.fecnac,self.pais))
            conexion.commit()
        except sqlite3.Error as e:
            print("Error al insertar en la base de datos:", e)
            conexion.rollback()  # Revertir cambios
        finally:
            conexion.close()
