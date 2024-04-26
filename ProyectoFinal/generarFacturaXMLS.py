import sqlite3
import openyxl


class FacturaExcel():

    def __init__(self, numeroFac):

        conexion = sqlite3.connect('database/usuarios.db')
        cursor = conexion.cursor()

        cursor.execute('SELECT * FROM facturas WHERE numeroFactura = ?', (numeroFac,))
        cliente = cursor.fetchall()




        #Creo un nuevo excel
        workbook = openyxl.Workbook()

