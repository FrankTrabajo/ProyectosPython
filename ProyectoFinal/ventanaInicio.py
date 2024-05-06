from tkinter import *
from tkinter import Label, LabelFrame, PhotoImage, Canvas
import sqlite3

import ventanaBuscarCliente
import ventanaCheckOut
import ventanaCheckIn
import ventanaFacturas
import ventanaReservas


class VentanaInicio:
    def __init__(self, ventana_menu):
        self.ventana_menu = ventana_menu
        self.ventana_inicio = Toplevel()
        self.ventana_inicio.title("Hostal Cruz Sol")
        self.ventana_inicio.resizable(1, 1)
        self.ventana_inicio.wm_iconbitmap('recursos/cruzSol.ico')
        self.ventana_inicio.geometry("1300x900+240+120")

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

        btn_buscar = Button(frame_opciones, text="BUSCAR CLIENTE", width=20, font=('Calibri', 14, 'bold'), command=self.accederBusqueda)
        btn_buscar.grid(row=2, column=0, pady=10, sticky="w")

        btn_factura = Button(frame_opciones, text="FACTURACION", width=20, font=('Calibri', 14, 'bold'), command=self.accederFacturas)
        btn_factura.grid(row=3, column=0, pady=10, sticky="w")

        btn_reservar = Button(frame_opciones, text="RESERVAS", width=20, font=('Calibri', 14, 'bold'), command=self.accederReserva)
        btn_reservar.grid(row=4, column=0, pady=10, sticky="w")

        btn_salir = Button(frame_opciones, text="SALIR", width=20, font=('Calibri', 14, 'bold'), command=self.salir)
        btn_salir.grid(row=5, column=0, pady=10, sticky="w")

        # Crear el marco para clientes activos
        self.frame_clientes = LabelFrame(self.ventana_inicio, text="", padx=350, pady=30 , borderwidth=1)
        self.frame_clientes.configure(labelanchor='s')
        self.frame_clientes.grid(row=1,column=1)

        # Crear la etiqueta dentro del marco
        self.haboc = Label(self.frame_clientes, text="HABITACIONES OCUPADAS", padx=0, pady=0, font=('Calibri', 14, 'bold'))
        # Centrar la etiqueta dentro del marco
        self.haboc.grid(row=2,column=0, rowspan=5)

        # Crear el marco para listado de clientes activos
        self.frame_clienteslista = LabelFrame(self.ventana_inicio, text="Clientes", font=('Calibri', 16, 'bold'))
        self.frame_clienteslista.grid(row=2,column=1, padx=10)

        # Etiquetas de encabezado
        self.etiqueta_nom_cli = Label(self.frame_clienteslista, text="Nombre", padx=55, pady=5, font=('Calibri', 11, 'bold'))
        self.etiqueta_nom_cli.grid(row=0, column=0)

        self.etiqueta_ape_cli = Label(self.frame_clienteslista, text="Apellidos", padx=55, pady=5, font=('Calibri', 11, 'bold'))
        self.etiqueta_ape_cli.grid(row=0, column=1)

        self.etiqueta_habita_cli = Label(self.frame_clienteslista, text="Habitacion", padx=55, pady=5, font=('Calibri', 11, 'bold'))
        self.etiqueta_habita_cli.grid(row=0, column=2)

        self.etiqueta_entra_cli = Label(self.frame_clienteslista, text="Fecha Entrada", padx=55, pady=5, font=('Calibri', 11, 'bold'))
        self.etiqueta_entra_cli.grid(row=0, column=3)

        self.etiqueta_sale_cli = Label(self.frame_clienteslista, text="Fecha Salida", padx=55, pady=5, font=('Calibri', 11, 'bold'))
        self.etiqueta_sale_cli.grid(row=0, column=4)

        self.etiqueta_nombre_cli = Label(self.frame_clienteslista, text="", padx=55, pady=5, font=('Calibri', 11), fg="green")
        self.etiqueta_nombre_cli.grid(row=1, column=0)

        self.etiqueta_apellido_cli = Label(self.frame_clienteslista, text="", padx=55, pady=5, font=('Calibri', 11), fg="green")
        self.etiqueta_apellido_cli.grid(row=1, column=1)

        self.etiqueta_hab_cli = Label(self.frame_clienteslista, text="", padx=55, pady=5, font=('Calibri', 11), fg="green")
        self.etiqueta_hab_cli.grid(row=1, column=2)

        self.etiqueta_ent_cli = Label(self.frame_clienteslista, text="", padx=55, pady=5, font=('Calibri', 11), fg="green")
        self.etiqueta_ent_cli.grid(row=1, column=3)

        self.etiqueta_sal_cli = Label(self.frame_clienteslista, text="", padx=55, pady=5, font=('Calibri', 11), fg="green")
        self.etiqueta_sal_cli.grid(row=1, column=4)

        self.actualizar_lista_clientes()

        #######################################################################################    RESERVAS    ########################
        # Crear el marco para clientes con reserva
        frame_reservas = LabelFrame(self.ventana_inicio, text="", padx=350, pady=30, width=200)
        frame_reservas.configure(labelanchor='s')
        frame_reservas.grid(row=3,column=1)


        # Crear la etiqueta dentro del marco
        self.reservas = Label(frame_reservas, text="RESERVAS", padx=0, pady=0, font=('Calibri', 14, 'bold'), borderwidth=1)
        # Centrar la etiqueta dentro del marco
        self.reservas.grid(row=4,column=0)

        # Crear el marco para listado de clientes activos
        self.frame_clientesreserva = LabelFrame(self.ventana_inicio, text="Clientes Con Reserva", font=('Calibri', 16, 'bold'))
        self.frame_clientesreserva.grid(row=6,column=1, padx=10)

        # Etiquetas de encabezado
        self.etiqueta_nom_res = Label(self.frame_clientesreserva, text="Nombre", padx=55, pady=5, font=('Calibri', 11, 'bold'))
        self.etiqueta_nom_res.grid(row=0, column=0)

        self.etiqueta_ape_res = Label(self.frame_clientesreserva, text="Apellidos", padx=55, pady=5, font=('Calibri', 11, 'bold'))
        self.etiqueta_ape_res.grid(row=0, column=1)

        self.etiqueta_habita_res = Label(self.frame_clientesreserva, text="Habitacion", padx=55, pady=5, font=('Calibri', 11, 'bold'))
        self.etiqueta_habita_res.grid(row=0, column=2)

        self.etiqueta_entra_res = Label(self.frame_clientesreserva, text="Fecha Entrada", padx=55, pady=5, font=('Calibri', 11, 'bold'))
        self.etiqueta_entra_res.grid(row=0, column=3)

        self.etiqueta_sale_res = Label(self.frame_clientesreserva, text="Fecha Salida", padx=55, pady=5, font=('Calibri', 11, 'bold'))
        self.etiqueta_sale_res.grid(row=0, column=4)

        self.etiqueta_nombre_res = Label(self.frame_clientesreserva, text="", padx=55, pady=5, font=('Calibri', 11), fg="orange")
        self.etiqueta_nombre_res.grid(row=1, column=0)

        self.etiqueta_apellido_res = Label(self.frame_clientesreserva, text="", padx=55, pady=5, font=('Calibri', 11), fg="orange")
        self.etiqueta_apellido_res.grid(row=1, column=1)

        self.etiqueta_hab_res = Label(self.frame_clientesreserva, text="", padx=55, pady=5, font=('Calibri', 11), fg="orange")
        self.etiqueta_hab_res.grid(row=1, column=2)

        self.etiqueta_ent_res = Label(self.frame_clientesreserva, text="", padx=55, pady=5, font=('Calibri', 11), fg="orange")
        self.etiqueta_ent_res.grid(row=1, column=3)

        self.etiqueta_sal_res = Label(self.frame_clientesreserva, text="", padx=55, pady=5, font=('Calibri', 11), fg="orange")
        self.etiqueta_sal_res.grid(row=1, column=4)


        self.actualizar_lista_reservas()

    def actualizar_lista_clientes(self):
        clientes = self.obtener_clientes_desde_bd()

        for widget in self.frame_clienteslista.winfo_children():
            widget.destroy()

        for i, cliente in enumerate(clientes, start=1):  # Comenzamos desde 1 para evitar reescribir encabezados
            nombre = cliente[0]
            apellidos = f"{cliente[1]} {cliente[2]}"
            habitacion = cliente[3]
            fechaentrada = cliente[4]
            fechasalida = cliente[5]


            # Actualizar las etiquetas
            nombre_cli = Label(self.frame_clienteslista, text=nombre, padx=55, pady=5, font=('Calibri', 11), fg="green")
            nombre_cli.grid(row=i, column=0)

            apellido_cli = Label(self.frame_clienteslista, text=apellidos, padx=55, pady=5, font=('Calibri', 11), fg="green")
            apellido_cli.grid(row=i, column=1)

            hab_cli = Label(self.frame_clienteslista, text=habitacion, padx=55, pady=5, font=('Calibri', 11), fg="green")
            hab_cli.grid(row=i, column=2)

            ent_cli = Label(self.frame_clienteslista, text=fechaentrada, padx=55, pady=5, font=('Calibri', 11), fg="green")
            ent_cli.grid(row=i, column=3)

            sal_cli = Label(self.frame_clienteslista, text=fechasalida, padx=55, pady=5, font=('Calibri', 11), fg="green")
            sal_cli.grid(row=i, column=4)

            # Actualizar las variables de instancia
            self.nombre_cliente = nombre
            self.apellidos_cliente = apellidos
            self.habitacion_cliente = habitacion
            self.fecha_entrada_cliente = fechaentrada
            self.fecha_salida_cliente = fechasalida


    def actualizar_lista_reservas(self):
        reservas = self.obtener_reservas_desde_bd()

        for i, cliente in enumerate(reservas, start=1):  # Comenzamos desde 1 para evitar reescribir encabezados
            nombreres = cliente[0]
            apellidosres = f"{cliente[1]} {cliente[2]}"
            habitacionres = cliente[3]
            fechaentradares = cliente[4]
            fechasalidares = cliente[5]

            # Actualizar las etiquetas
            nombre_res = Label(self.frame_clientesreserva, text=nombreres, padx=55, pady=5, font=('Calibri', 11), fg="orange")
            nombre_res.grid(row=i, column=0)

            apellido_res = Label(self.frame_clientesreserva, text=apellidosres, padx=55, pady=5, font=('Calibri', 11), fg="orange")
            apellido_res.grid(row=i, column=1)

            hab_res = Label(self.frame_clientesreserva, text=habitacionres, padx=55, pady=5, font=('Calibri', 11), fg="orange")
            hab_res.grid(row=i, column=2)

            ent_res = Label(self.frame_clientesreserva, text=fechaentradares, padx=55, pady=5, font=('Calibri', 11), fg="orange")
            ent_res.grid(row=i, column=3)

            sal_res = Label(self.frame_clientesreserva, text=fechasalidares, padx=55, pady=5, font=('Calibri', 11), fg="orange")
            sal_res.grid(row=i, column=4)

            # Configurar las etiquetas existentes
            self.etiqueta_nombre_res.config(text=nombreres, fg="orange")
            self.etiqueta_apellido_res.config(text=apellidosres, fg="orange")
            self.etiqueta_hab_res.config(text=habitacionres, fg="orange")
            self.etiqueta_ent_res.config(text=fechaentradares, fg="orange")
            self.etiqueta_sal_res.config(text=fechasalidares, fg="orange")

            # Actualizar las variables de instancia
            self.nombre_reserva = nombreres
            self.apellidos_reserva = apellidosres
            self.habitacion_reserva = habitacionres
            self.fecha_entrada_reserva = fechaentradares
            self.fecha_salida_reserva = fechasalidares


    def accederCheckIn(self):
        self.checkIn = ventanaCheckIn.CheckIn(self)

    def accederCheckOut(self):
        self.checkOut = ventanaCheckOut.CheckOut(self)

    def accederReserva(self):
        self.reserva = ventanaReservas.Reserva(self)

    def accederBusqueda(self):
        self.busqueda = ventanaBuscarCliente.BuscaCliente(self)

    def accederFacturas(self):
        self.facturas = ventanaFacturas.Factura(self)

    def obtener_clientes_desde_bd(self):
        # Establecer conexión a la base de datos
        conexion = sqlite3.connect('database/usuarios.db')
        cursor = conexion.cursor()

        # Ejecutar la consulta para obtener los clientes
        cursor.execute("SELECT nombre, apellido1, apellido2, habitacion, fecEnt, fecSal FROM clientesTEMP")
        clientes = cursor.fetchall()

        # Cerrar la conexión
        conexion.close()

        return clientes

    def obtener_reservas_desde_bd(self):
        # Establecer conexión a la base de datos
        conexion = sqlite3.connect('database/usuarios.db')
        cursor = conexion.cursor()

        # Ejecutar la consulta para obtener los clientes
        cursor.execute("SELECT nombre, apellido1, apellido2, habitacion, fechaEntrada, fechaSalida FROM clientesReserva")
        reservas = cursor.fetchall()

        # Cerrar la conexión
        conexion.close()

        return reservas

    def salir(self):
        self.ventana_inicio.destroy()
