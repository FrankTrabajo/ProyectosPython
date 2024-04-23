from tkinter import *
from tkinter import Label, LabelFrame, PhotoImage, Canvas
import sqlite3

import ventanaCheckOut
import ventanaCheckIn
import ventanaReservas


class VentanaInicio:
    def __init__(self, ventana_menu):
        self.ventana_inicio = ventana_menu
        self.ventana_inicio = Toplevel()
        self.ventana_inicio.title("Hostal Cruz Sol")
        self.ventana_inicio.resizable(1, 1)
        self.ventana_inicio.wm_iconbitmap('recursos/cruzSol.ico')
        self.ventana_inicio.geometry("1200x600+240+120")

        # Creación del contenedor Frame principal
        titulo = Label(self.ventana_inicio, text="INICIO", font=('Calibri', 16, 'bold'), fg='#000080')
        titulo.grid(row=0, column=0)

        # Creación de un contenedor Canvas para la imagen
        frame_imagen = LabelFrame(self.ventana_inicio, text="", font=('Calibri', 16, 'bold'), padx=50, pady=10, borderwidth=1)
        frame_imagen.configure(labelanchor='w')
        frame_imagen.grid(row=1, column=0)

        # Carga de la imagen
        self.filename = PhotoImage(file='recursos/cruzSol.png')
        canvas = Canvas(frame_imagen, width=150, height=80)
        canvas.create_image(80, 0, anchor='n', image=self.filename)
        canvas.grid(row=0, column=0)

        # Crear el marco para los botones
        frame_opciones = LabelFrame(self.ventana_inicio, text="", padx=20, pady=40)
        frame_opciones.configure(labelanchor='w')
        frame_opciones.grid(row=2, column=0)

        # Crear los botones y alinearlos a la izquierda
        btn_checkin = Button(frame_opciones, text="CHECKIN", width=20, font=('Calibri', 14, 'bold'), command=self.accederCheckIn)
        btn_checkin.grid(row=0, column=0, pady=10, sticky="w")

        btn_checkout = Button(frame_opciones, text="CHECKOUT", width=20, font=('Calibri', 14, 'bold'), command=self.accederCheckOut)
        btn_checkout.grid(row=1, column=0, pady=10, sticky="w")

        btn_buscar = Button(frame_opciones, text="BUSCAR CLIENTE", width=20, font=('Calibri', 14, 'bold'))
        btn_buscar.grid(row=2, column=0, pady=10, sticky="w")

        btn_factura = Button(frame_opciones, text="FACTURACION", width=20, font=('Calibri', 14, 'bold'))
        btn_factura.grid(row=3, column=0, pady=10, sticky="w")

        btn_reservar = Button(frame_opciones, text="RESERVAS", width=20, font=('Calibri', 14, 'bold'), command=self.accederReserva)
        btn_reservar.grid(row=4, column=0, pady=10, sticky="w")

        btn_salir = Button(frame_opciones, text="SALIR", width=20, font=('Calibri', 14, 'bold'), command=self.salir)
        btn_salir.grid(row=5, column=0, pady=10, sticky="w")

        # Crear el marco para clientes activos
        frame_clientes = LabelFrame(self.ventana_inicio, text="", padx=350, pady=30)
        frame_clientes.configure(labelanchor='s')
        frame_clientes.grid(row=1,column=1)

        # Crear la etiqueta dentro del marco
        self.haboc = Label(frame_clientes, text="HABITACIONES OCUPADAS", padx=0, pady=0, font=('Calibri', 14, 'bold'))
        # Centrar la etiqueta dentro del marco
        self.haboc.grid(row=0,column=0, rowspan=5)

        # Crear el marco para listado de clientes activos
        self.frame_clienteslista = LabelFrame(self.ventana_inicio, text="Clientes", font=('Calibri', 16, 'bold'))
        self.frame_clienteslista.grid(row=2,column=1, padx=10, pady=10)

        # Etiquetas de encabezado
        self.etiqueta_nombre_cli = Label(self.frame_clienteslista, text="Nombre", padx=55, pady=5, font=('Calibri', 11, 'bold'))
        self.etiqueta_nombre_cli.grid(row=0, column=0)

        self.etiqueta_apellido_cli = Label(self.frame_clienteslista, text="Apellidos", padx=55, pady=5, font=('Calibri', 11, 'bold'))
        self.etiqueta_apellido_cli.grid(row=0, column=1)

        self.etiqueta_hab_cli = Label(self.frame_clienteslista, text="Habitacion", padx=55, pady=5, font=('Calibri', 11, 'bold'))
        self.etiqueta_hab_cli.grid(row=0, column=2)

        self.actualizar_lista_clientes()

    def actualizar_lista_clientes(self):
        clientes = self.obtener_clientes_desde_bd()

        # Limpiar las etiquetas antiguas
        for widget in self.frame_clienteslista.winfo_children():
            widget.destroy()

        for i, cliente in enumerate(clientes, start=1):  # Comenzamos desde 1 para evitar reescribir encabezados
            nombre = cliente[0]
            apellidos = f"{cliente[1]} {cliente[2]}"
            habitacion = cliente[3]

            # Actualizar las etiquetas
            nombre_cli = Label(self.frame_clienteslista, text=nombre, padx=55, pady=5, font=('Calibri', 11))
            nombre_cli.grid(row=i, column=0)

            apellido_cli = Label(self.frame_clienteslista, text=apellidos, padx=55, pady=5, font=('Calibri', 11))
            apellido_cli.grid(row=i, column=1)

            hab_cli = Label(self.frame_clienteslista, text=habitacion, padx=55, pady=5, font=('Calibri', 11))
            hab_cli.grid(row=i, column=2)

    def accederCheckIn(self):
        self.checkIn = ventanaCheckIn.CheckIn(self)

    def accederCheckOut(self):
        self.checkOut = ventanaCheckOut.CheckOut(self)

    def accederReserva(self):
        self.reserva = ventanaReservas.Reserva(self)


    def obtener_clientes_desde_bd(self):
        # Establecer conexión a la base de datos
        conexion = sqlite3.connect('database/usuarios.db')
        cursor = conexion.cursor()

        # Ejecutar la consulta para obtener los clientes
        cursor.execute("SELECT nombre, apellido1, apellido2, habitacion FROM clientesTEMP")
        clientes = cursor.fetchall()

        # Cerrar la conexión
        conexion.close()

        return clientes

    def salir(self):
        self.ventana_inicio.destroy()
