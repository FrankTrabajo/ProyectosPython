import sqlite3


class Cliente:

    def __init__(self, tipodoc, numdoc, fecexpdoc, nombre, apellido1, apellido2, pais, fecnac, habitacion, fecEnt, fecSal, personas):
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
        self.personas = personas




    def registrarCliente(self):
        conexion = sqlite3.connect('database/usuarios.db')
        cursor = conexion.cursor()

        try:
            cursor.execute('INSERT INTO clientesTEMP VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', (self.tipodoc,self.numdoc,self.fecexpdoc,self.nombre,self.apellido1,self.apellido2,self.fecnac,self.pais,self.habitacion, self.fecent, self.fecsal, self.personas))
            conexion.commit()
            conexion.close()
        except sqlite3.Error as e:
            print("Error al insertar en la base de datos:", e)
            conexion.rollback()  # Revertir cambios
        finally:
            conexion.close()


class ClienteReserva():

    def __init__(self, tipodoc, numdoc, nombre, apellido1, apellido2, pais, fecnac):
        self.tipodoc = tipodoc
        self.numdoc = numdoc
        self.nombre = nombre
        self.apellido1 = apellido1
        if apellido2 != "":
            self.apellido2 = apellido2
        else:
            self.apellido2 = ""
        self.pais = pais
        self.fecnac = fecnac

    def registrarClienteReserva(self):
        conexion = sqlite3.connect('database/usuarios.db')
        cursor = conexion.cursor()

        try:
            cursor.execute('INSERT INTO clientesPER VALUES (?,?,?,?,?,?,?)', (self.tipodoc,self.numdoc,self.nombre,self.apellido1,self.apellido2,self.fecnac,self.pais))
            conexion.commit()
            conexion.close()
        except sqlite3.Error as e:
            print("Error al insertar en la base de datos:", e)
            conexion.rollback()  # Revertir cambios
        finally:
            conexion.close()
