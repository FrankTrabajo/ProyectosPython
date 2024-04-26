import datetime
from tkinter import *
import sqlite3

class Factura():
    def __init__(self, ventana_inicio):
        self.ventana_inicio = ventana_inicio
        self.ventana_factura = Toplevel()
        self.ventana_factura.title("Hostal Cruz Sol")
        self.ventana_factura.resizable(1, 1)
        self.ventana_factura.wm_iconbitmap('recursos/cruzSol.ico')
        self.ventana_factura.geometry("1300x600+240+120")

        titulo = Label(self.ventana_factura, text="FACTURAS", font=('Calibri', 16, 'bold'), fg='#000080')
        titulo.grid(row=0,column=0)

        self.frame_datos_factura = LabelFrame(self.ventana_factura, text="Datos de facturacion")
        self.frame_datos_factura.grid(row=1,column=0)

        ##  NOMBRE Y APELLIDO -> CAMPO RELLENADO DE BBDD
        self.etiqueta_nombre = Label(self.frame_datos_factura, text="Nombre:")
        self.etiqueta_nombre.grid(row=1, column=0)

        self.nombre = Entry(self.frame_datos_factura)
        self.nombre.grid(row=1, column=1, pady=5, padx=5)
        ##  NIF -> CAMPO RELLENADO DE BBDD
        self.etiqueta_nif = Label(self.frame_datos_factura, text="NIF: ")
        self.etiqueta_nif.grid(row=2,column=0)

        self.nif = Entry(self.frame_datos_factura)
        self.nif.grid(row=2, column=1)
        ##  DIRECCION
        self.etiqueta_direccion = Label(self.frame_datos_factura, text="Direccion: ")
        self.etiqueta_direccion.grid(row=3,column=0)

        self.direccion = Entry(self.frame_datos_factura)
        self.direccion.grid(row=3, column=1)
        ##  CP
        self.etiqueta_cp = Label(self.frame_datos_factura, text="CP: ")
        self.etiqueta_cp.grid(row=4,column=0)

        self.cp = Entry(self.frame_datos_factura)
        self.cp.grid(row=4, column=1)
        ##  LOCALIDAD
        self.etiqueta_localidad = Label(self.frame_datos_factura, text="Localidad: ")
        self.etiqueta_localidad.grid(row=5,column=0)

        self.localidad = Entry(self.frame_datos_factura)
        self.localidad.grid(row=5, column=1)
        ##  PAIS -> CAMPO RELLENADO DE BBDD
        self.etiqueta_pais = Label(self.frame_datos_factura, text="Pais: ")
        self.etiqueta_pais.grid(row=6,column=0)

        self.pais = Entry(self.frame_datos_factura)
        self.pais.grid(row=6, column=1)
        ##  PERSONAS -> CAPO RELLENADO DE BBDD
        self.etiqueta_personas = Label(self.frame_datos_factura, text="Personas: ")
        self.etiqueta_personas.grid(row=7,column=0)

        self.personas = Entry(self.frame_datos_factura)
        self.personas.grid(row=7, column=1)
        ##  FECHA LLEGADA -> CAMPO RELLENADO DE BBDD
        self.etiqueta_fechaLlegada = Label(self.frame_datos_factura, text="Fecha de llegada: ")
        self.etiqueta_fechaLlegada.grid(row=8,column=0)

        self.fechaLlegada = Entry(self.frame_datos_factura)
        self.fechaLlegada.grid(row=8, column=1)
        ##  FECHA SALIDA -> CAMPO RELLENADO DE BBDD
        self.etiqueta_fechaSalida = Label(self.frame_datos_factura, text="Fecha de salida: ")
        self.etiqueta_fechaSalida.grid(row=9,column=0)

        self.fechaSalida = Entry(self.frame_datos_factura)
        self.fechaSalida.grid(row=9, column=1)
        ##HABITACIONES
        self.etiqueta_habitacion = Label(self.frame_datos_factura, text='Habitacion:')
        self.etiqueta_habitacion.grid(row=10, column=0)

        habitaciones_ocupadas = self.obtener_habitaciones_ocupadas()
        self.habitacion = StringVar(self.frame_datos_factura)

        self.habitacionMenu = OptionMenu(self.frame_datos_factura, self.habitacion, *habitaciones_ocupadas, command=self.mostrarCliente)
        self.habitacionMenu.grid(row=10, column=1, padx=10, pady=5)
        ##  NUMERO DE FACTURA -> CAMPO AUTOMATICO SACADO DE BBDD
        self.etiqueta_numeroFactura = Label(self.frame_datos_factura, text="Numero de factura: ")
        self.etiqueta_numeroFactura.grid(row=11,column=0)

        self.numeroFactura = Entry(self.frame_datos_factura)
        self.numeroFactura.grid(row=11, column=1)

        ##BOTON PARA GUARDAR
        btn_guardar = Button(self.frame_datos_factura, text="Guardar", width=10, font=('Calibri', 14, 'bold'),command=self.btn_guardar)
        btn_guardar.grid(row=12, column=0, pady=10)

        ##BOTON PARA SALIR AL MENU PRINCIPAL
        btn_salir = Button(self.frame_datos_factura, text="Salir", width=10, font=('Calibri', 14, 'bold'), command=self.btn_salir)
        btn_salir.grid(row=12, column=1, pady=10)


    def obtener_habitaciones_ocupadas(self):
        # Conectar a la base de datos
        conexion = sqlite3.connect('database/usuarios.db')
        cursor = conexion.cursor()

        # Consulta para obtener los números de habitaciones que no están ocupadas
        cursor.execute("SELECT numeroHab FROM habitacion WHERE ocupada = 1")
        habitaciones_libres = cursor.fetchall()

        # Cerrar la conexión
        conexion.close()

        # Devolver la lista de habitaciones libres
        return [habitacion[0] for habitacion in habitaciones_libres]


    def mostrarCliente(self, habitacionSeleccionada):
        conexion = sqlite3.connect('database/usuarios.db')
        cursor = conexion.cursor()

        cursor.execute('SELECT * FROM clientesTEMP WHERE habitacion = ?', (habitacionSeleccionada,))
        cliente = cursor.fetchall()
        cursor.execute('SELECT numeroFactura FROM facturas WHERE habitacion = ?', (habitacionSeleccionada,))
        factura = cursor.fetchall()
        if not factura:
            self.numeroFactura.delete(0,END)
            self.numeroFactura.insert(0,1)

        if cliente:
            cliente = cliente[0]  # Tomamos solo la primera fila si hay resultados

            self.nombre.delete(0, END)
            self.nombre.insert(0, f"{cliente[3]} {cliente[4]} {cliente[5]}")
            self.nif.delete(0,END)
            self.nif.insert(0, f"{cliente[0]} {cliente[1]}")
            self.pais.delete(0, END)
            self.pais.insert(0,cliente[7])
            self.personas.delete(0,END)
            self.personas.insert(0,cliente[11])
            self.fechaLlegada.delete(0,END)
            self.fechaLlegada.insert(0,cliente[9])
            self.fechaSalida.delete(0,END)
            self.fechaSalida.insert(0,cliente[10])

            self.calcularPrecio(habitacionSeleccionada)

        conexion.close()


    def calcularPrecio(self, habitacion):
        conexion = sqlite3.connect('database/usuarios.db')
        cursor = conexion.cursor()

        cursor.execute('SELECT precio FROM Habitacion WHERE NumeroHab = ?', (habitacion,))
        precioHab = cursor.fetchone()

        fechallegada = self.fechaLlegada.get()
        fechasalida = self.fechaSalida.get()

        try:
            fechallegada_datetime = datetime.datetime.strptime(fechallegada, "%d/%m/%Y")
            fechasalida_datetime = datetime.datetime.strptime(fechasalida, "%d/%m/%Y")
            dias = (fechasalida_datetime - fechallegada_datetime).days
            precio = precioHab[0] * dias
            return precio
        except ValueError as e:
            print("Error al convertir las fechas:", e)
        except Exception as ex:
            print("Ocurrió un error:", ex)
        finally:
            conexion.close()



    def btn_salir(self):
        self.ventana_factura.destroy()

    def btn_guardar(self):

        nombre = self.nombre.get()
        nif = self.nif.get()
        direccion = self.direccion.get()
        cp = self.cp.get()
        localidad = self.localidad.get()
        pais = self.pais.get()
        personas = self.personas.get()
        llegada = self.fechaLlegada.get()
        salida = self.fechaSalida.get()
        habitacion = self.habitacion.get()
        precio = self.calcularPrecio(habitacion)
        print(precio)

        conexion = sqlite3.connect('database/usuarios.db')
        cursor = conexion.cursor()

        cursor.execute('INSERT INTO facturas (nombre, nif, direccion, cp, localidad, pais, personas, llegada, salida, habitacion, precio) VALUES (?,?,?,?,?,?,?,?,?,?,?)', (nombre,nif,direccion,cp,localidad,pais,personas,llegada,salida,habitacion,precio))
        conexion.commit()
        conexion.close()
