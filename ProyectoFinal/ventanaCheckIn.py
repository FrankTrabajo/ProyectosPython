from tkinter import *
from tkinter import Label, LabelFrame, Entry
from tkcalendar import Calendar
import sqlite3
import cliente


class CheckIn:

    def __init__(self, ventana_inicio):
        self.ventana_inicio = ventana_inicio
        self.ventana_check = Toplevel()
        self.ventana_check.title("Hostal Cruz Sol")
        self.ventana_check.resizable(1, 1)  # Activa la redimension de la ventana. Para desactivarla (0,0)
        self.ventana_check.wm_iconbitmap('recursos/cruzSol.ico')
        self.ventana_check.geometry("390x520+240+120")

        self.opciones = ['DNI', 'NIF', 'PASAPORTE']

        # Creacion del contenedor Frame principal
        titulo = Label(self.ventana_check, text="CHECKIN", font=('Calibri', 16, 'bold'), fg='#000080')
        titulo.grid(row=0, column=0)

        self.datos_reserva = LabelFrame(self.ventana_check, text="DATOS CLIENTE", font=('Calibri', 16, 'bold'))
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

        self.expdoc = Entry(self.datos_reserva, font=('Calibri', 13), validate="key")
        self.expdoc.grid(row=2,column=1, padx=5, pady=5)

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
        self.etiqueta_fecnac = Label(self.datos_reserva, text='Fecha de nacimiento:')
        self.etiqueta_fecnac.grid(row=7, column=0)

        self.fecnac = Entry(self.datos_reserva, font=('Calibri', 13), validate="key")
        self.fecnac.grid(row=7,column=1, padx=5, pady=5)


        ##HABITACIONES
        self.etiqueta_habitacion = Label(self.datos_reserva, text='Habitacion:')
        self.etiqueta_habitacion.grid(row=8, column=0)

        habitaciones_libres = self.obtener_habitaciones_libres()
        self.habitacion = StringVar(self.datos_reserva)
        self.habitacion.set(habitaciones_libres[0])  # Establecer el valor predeterminado

        # Configurar el OptionMenu para usar los números de habitaciones libres
        self.habitacionMenu = OptionMenu(self.datos_reserva, self.habitacion, *habitaciones_libres)
        self.habitacionMenu.grid(row=8, column=1, padx=10, pady=5)

        ##FECHA DE ESTANCIA
        self.etiqueta_entrada = Label(self.datos_reserva, text='Fecha de entrada:')
        self.etiqueta_entrada.grid(row=9, column=0)

        self.estancia = Entry(self.datos_reserva, font=('Calibri', 13), validate="key")
        self.estancia.grid(row=9,column=1, padx=5, pady=5)


        ##FECHA FIN ESTANCIA
        self.etiqueta_salida = Label(self.datos_reserva, text='Fecha de salida:')
        self.etiqueta_salida.grid(row=10, column=0)

        self.salida = Entry(self.datos_reserva, font=('Calibri', 13), validate="key")
        self.salida.grid(row=10,column=1, padx=5, pady=5)


        ##BOTON PARA GUARDAR LA RESERVA
        btn_guardar = Button(self.datos_reserva, text="Guardar", width=10, font=('Calibri', 14, 'bold'),command=self.btn_guardar)
        btn_guardar.grid(row=11, column=0, pady=10)

        ##BOTON PARA SALIR AL MENU PRINCIPAL
        btn_salir = Button(self.datos_reserva, text="Salir", width=10, font=('Calibri', 14, 'bold'), command=self.btn_salir)
        btn_salir.grid(row=11, column=1, pady=10)


    def btn_salir(self):
        self.ventana_check.destroy()

    def btn_guardar(self):
        tipodoc = self.opcion.get()
        numdoc = self.numdoc.get()
        fecExp = self.expdoc.get()
        nombre = self.nombre.get()
        apellido1 = self.apellido1.get()
        apellido2 = self.apellido2.get()
        pais = self.pais.get()
        fecNac = self.fecnac.get()
        fecEnt = self.estancia.get()
        fecSal = self.salida.get()
        habitacion = self.habitacion.get()
        print(fecNac,":",fecExp)
        print(nombre)
        cli = cliente.Cliente(tipodoc,numdoc,fecExp,nombre,apellido1,apellido2,pais,fecNac,habitacion, fecEnt, fecSal)
        cliReserva = cliente.ClienteReserva(tipodoc,numdoc,nombre,apellido1,apellido2,fecNac,pais)
        cli.registrarCliente()
        cliReserva.registrarClienteReserva()
        self.definirHabOcupada(habitacion)

        self.ventana_inicio.etiqueta_nombre_cli.config(text=nombre, fg="green")
        self.ventana_inicio.etiqueta_apellido_cli.config(text=f"{apellido1} {apellido2}", fg="green")
        self.ventana_inicio.etiqueta_hab_cli.config(text=habitacion, fg="green")
        self.ventana_inicio.etiqueta_ent_cli.config(text=fecEnt, fg="green")
        self.ventana_inicio.etiqueta_sal_cli.config(text=fecSal, fg="green")
        self.ventana_check.destroy()


    def definirHabOcupada(self, numHab):
        # Establecer conexión a la base de datos
        conexion = sqlite3.connect('database/usuarios.db')
        cursor = conexion.cursor()

        # Actualizar el estado de la habitación a ocupada
        cursor.execute("UPDATE habitacion SET ocupada = 1 WHERE numeroHab = ?", (numHab,))

        # Confirmar el cambio en la base de datos
        conexion.commit()

        # Cerrar la conexión
        conexion.close()

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
