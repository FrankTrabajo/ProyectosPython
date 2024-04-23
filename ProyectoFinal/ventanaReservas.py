from tkinter import *
import sqlite3

class Reserva:

    def __init__ (self, ventana_inicio):
        self.ventana_inicio = ventana_inicio
        self.ventana_reserva = Toplevel()
        self.ventana_reserva.title("Hostal Cruz Sol")
        self.ventana_reserva.resizable(1, 1)  # Activa la redimension de la ventana. Para desactivarla (0,0)
        self.ventana_reserva.wm_iconbitmap('recursos/cruzSol.ico')
        self.ventana_reserva.geometry("1065x450+240+120")

        self.opciones = ['DNI', 'NIF', 'PASAPORTE']

        titulo = Label(self.ventana_reserva, text="RESERVAS", font=('Calibri', 16, 'bold'), fg='#000080')
        titulo.grid(row=0, column=0)

        self.datos_reserva = LabelFrame(self.ventana_reserva, text="DATOS DE LA RESERVA", font=('Calibri', 16, 'bold'))
        self.datos_reserva.grid(row=1, column=0, padx=10)

        self.etiqueta_tipo = Label(self.datos_reserva, text='Tipo Documento:')
        self.etiqueta_tipo.grid(row=0, column=0)

        self.opcion = StringVar(self.datos_reserva)
        self.opcion.set(self.opciones[0])
        self.opcionMenu = OptionMenu(self.datos_reserva, self.opcion, *self.opciones)
        self.opcionMenu.grid(row=1, column=0, padx=10, pady=5)

        self.numdoc = Entry(self.datos_reserva, font=('Calibri', 13))
        self.numdoc.grid(row=1, column=1, padx=5, pady=5)

        ##FECHA DE EXPEDICION DE DOCUMENTO
        self.etiqueta_expdoc = Label(self.datos_reserva, text='Fecha Expiracion Documento:')
        self.etiqueta_expdoc.grid(row=2, column=0)

        self.etiqueta_dia = Label(self.datos_reserva, text='Dia:')
        self.etiqueta_dia.grid(row=2, column=1, padx=5, pady=5)

        self.dia = Entry(self.datos_reserva, font=('Calibri', 13), validate="key")
        self.dia.grid(row=2,column=2, padx=5, pady=5)

        self.etiqueta_mes = Label(self.datos_reserva, text='Mes:')
        self.etiqueta_mes.grid(row=2, column=3, padx=5, pady=5)

        self.mes = Entry(self.datos_reserva, font=('Calibri', 13), validate="key")
        self.mes.grid(row=2,column=4, padx=5, pady=5)

        self.etiqueta_año = Label(self.datos_reserva, text='Año:')
        self.etiqueta_año.grid(row=2, column=5, padx=5, pady=5)

        self.año = Entry(self.datos_reserva, font=('Calibri', 13), validate="key")
        self.año.grid(row=2,column=6, padx=5, pady=5)

        ##NOMBRE
        self.etiqueta_nombre = Label(self.datos_reserva, text='Nombre:')
        self.etiqueta_nombre.grid(row=3, column=0)

        self.nombre = Entry(self.datos_reserva, font=('Calibri', 13))
        self.nombre.grid(row=3, column=1, padx=10, pady=5)

        ##APELLIDO
        self.etiqueta_apellido1 = Label(self.datos_reserva, text='Primer apellido:')
        self.etiqueta_apellido1.grid(row=4, column=0)

        self.apellido1 = Entry(self.datos_reserva, font=('Calibri', 13))
        self.apellido1.grid(row=4, column=1, padx=10, pady=5)

        ##SEGUNDO APELLIDO
        self.etiqueta_apellido2 = Label(self.datos_reserva, text='Segundo apellido:')
        self.etiqueta_apellido2.grid(row=5, column=0)

        self.apellido2 = Entry(self.datos_reserva, font=('Calibri', 13))
        self.apellido2.grid(row=5, column=1, padx=10, pady=5)

        ##PAIS
        self.etiqueta_pais = Label(self.datos_reserva, text='Pais:')
        self.etiqueta_pais.grid(row=6, column=0)

        self.pais = Entry(self.datos_reserva, font=('Calibri', 13))
        self.pais.grid(row=6, column=1, padx=10, pady=5)

        ##FECHA DE NACIMIENTO
        self.etiqueta_expdoc = Label(self.datos_reserva, text='Fecha de nacimiento:')
        self.etiqueta_expdoc.grid(row=7, column=0)

        self.etiqueta_dia2 = Label(self.datos_reserva, text='Dia:')
        self.etiqueta_dia2.grid(row=7, column=1, padx=0, pady=5)

        self.dia2 = Entry(self.datos_reserva, font=('Calibri', 13), validate="key")
        self.dia2.grid(row=7,column=2, padx=5, pady=5)

        self.etiqueta_mes2 = Label(self.datos_reserva, text='Mes:')
        self.etiqueta_mes2.grid(row=7, column=3, padx=5, pady=5)

        self.mes2 = Entry(self.datos_reserva, font=('Calibri', 13), validate="key")
        self.mes2.grid(row=7,column=4, padx=5, pady=5)

        self.etiqueta_año2 = Label(self.datos_reserva, text='Año:')
        self.etiqueta_año2.grid(row=7, column=5, padx=5, pady=5)

        self.año2 = Entry(self.datos_reserva, font=('Calibri', 13), validate="key")
        self.año2.grid(row=7,column=6, padx=5, pady=5)


        ##HABITACIONES
        self.etiqueta_habitacion = Label(self.datos_reserva, text='Habitacion:')
        self.etiqueta_habitacion.grid(row=8, column=0)

        habitaciones_libres = self.obtener_habitaciones_libres()
        self.habitacion = StringVar(self.datos_reserva)
        self.habitacion.set(habitaciones_libres[0])  # Establecer el valor predeterminado

        # Configurar el OptionMenu para usar los números de habitaciones libres
        self.habitacionMenu = OptionMenu(self.datos_reserva, self.habitacion, *habitaciones_libres)
        self.habitacionMenu.grid(row=8, column=1, padx=10, pady=5)

        ##BOTON PARA GUARDAR LA RESERVA
        btn_guardar = Button(self.datos_reserva, text="Guardar", width=10, font=('Calibri', 14, 'bold'))
        btn_guardar.grid(row=9, column=0, pady=10)

        ##BOTON PARA SALIR AL MENU PRINCIPAL
        btn_salir = Button(self.datos_reserva, text="Salir", width=10, font=('Calibri', 14, 'bold'), command=self.btn_salir)
        btn_salir.grid(row=9, column=1, pady=10)


    def obtener_habitaciones_libres(self):
        # Conectar a la base de datos
        conexion = sqlite3.connect('database/usuarios.db')
        cursor = conexion.cursor()

        # Consulta para obtener los números de habitaciones que no están ocupadas
        cursor.execute("SELECT numeroHab FROM habitacion WHERE ocupada = 0")
        habitaciones_libres = cursor.fetchall()

        # Cerrar la conexión
        conexion.close()

        # Devolver la lista de habitaciones libres
        return [habitacion[0] for habitacion in habitaciones_libres]



    def btn_salir(self):
        self.ventana_reserva.destroy()
