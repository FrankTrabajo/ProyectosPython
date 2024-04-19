from tkinter import *
from tkinter import Label, LabelFrame, Entry
from tkcalendar import Calendar

import cliente


class CheckIn:

    def __init__(self, ventana_inicio):
        self.ventana_check = ventana_inicio
        self.ventana_check = Toplevel()
        self.ventana_check.title("Hostal Cruz Sol")
        self.ventana_check.resizable(1, 1)  # Activa la redimension de la ventana. Para desactivarla (0,0)
        self.ventana_check.wm_iconbitmap('recursos/cruzSol.ico')
        self.ventana_check.geometry("465x800+240+120")

        self.opciones = ['Tipo de Documento','DNI', 'NIF', 'PASAPORTE']

        # Creacion del contenedor Frame principal
        titulo = Label(self.ventana_check, text="CHECKIN", font=('Calibri', 16, 'bold'), fg='#000080')
        titulo.grid(row=0, column=0)

        toma_datos = LabelFrame(self.ventana_check, text="DATOS CLIENTE", font=('Calibri', 16, 'bold'))
        toma_datos.grid(row=1, column=0, padx=10)

        self.etiqueta_tipo = Label(toma_datos, text='Tipo Documento:')
        self.etiqueta_tipo.grid(row=0, column=0)

        self.opcion = StringVar(toma_datos)
        self.opcion.set(self.opciones[0])
        self.opcionMenu = OptionMenu(toma_datos, self.opcion, *self.opciones)
        self.opcionMenu.grid(row=1, column=0, padx=10, pady=5)

        self.numdoc = Entry(toma_datos, font=('Calibri', 13))
        self.numdoc.grid(row=1, column=1, padx=5, pady=5)

        ##FECHA DE EXPEDICION DE DOCUMENTO
        self.etiqueta_expdoc = Label(toma_datos, text='Fecha Expiracion Documento:')
        self.etiqueta_expdoc.grid(row=2, column=0)

        self.etiqueta_dia = Label(toma_datos, text='Dia:')
        self.etiqueta_dia.grid(row=2, column=1, padx=5, pady=5)

        self.dia = Entry(toma_datos, font=('Calibri', 13), validate="key")
        self.dia.grid(row=2,column=2, padx=5, pady=5)
        self.dia.config(validatecommand=(self.toma_datos.register(self.validate_entry), '%P'))
        self.dia.config(maxlength=2)

        self.etiqueta_mes = Label(toma_datos, text='Mes:')
        self.etiqueta_mes.grid(row=2, column=3, padx=5, pady=5)

        self.mes = Entry(toma_datos, font=('Calibri', 13), validate="key")
        self.mes.grid(row=2,column=4, padx=5, pady=5)
        self.mes.config(validatecommand=(self.toma_datos.register(self.validate_entry), '%P'))
        self.mes.config(maxlength=2)

        self.etiqueta_año = Label(toma_datos, text='Año:')
        self.etiqueta_año.grid(row=2, column=5, padx=5, pady=5)

        self.año = Entry(toma_datos, font=('Calibri', 13), validate="key")
        self.año.grid(row=2,column=6, padx=5, pady=5)
        self.año.config(validatecommand=(self.toma_datos.register(self.validate_entry), '%P'))
        self.año.config(maxlength=4)

        ##NOMBRE
        self.etiqueta_nombre = Label(toma_datos, text='Nombre:')
        self.etiqueta_nombre.grid(row=3, column=0)

        self.nombre = Entry(toma_datos, font=('Calibri', 13))
        self.nombre.grid(row=3, column=1, padx=10, pady=5)
        self.nombre.config(validate="key", validatecommand=(self.toma_datos.register(self.validate_input), '%P'))

        ##APELLIDO
        self.etiqueta_apellido1 = Label(toma_datos, text='Primer apellido:')
        self.etiqueta_apellido1.grid(row=4, column=0)

        self.apellido1 = Entry(toma_datos, font=('Calibri', 13))
        self.apellido1.grid(row=4, column=1, padx=10, pady=5)
        self.apellido1.config(validate="key", validatecommand=(self.toma_datos.register(self.validate_input), '%P'))

        ##SEGUNDO APELLIDO
        self.etiqueta_apellido2 = Label(toma_datos, text='Segundo apellido:')
        self.etiqueta_apellido2.grid(row=5, column=0)

        self.apellido2 = Entry(toma_datos, font=('Calibri', 13))
        self.apellido2.grid(row=5, column=1, padx=10, pady=5)
        self.apellido2.config(validate="key", validatecommand=(self.toma_datos.register(self.validate_input), '%P'))

        ##PAIS
        self.etiqueta_pais = Label(toma_datos, text='Pais:')
        self.etiqueta_pais.grid(row=6, column=0)

        self.pais = Entry(toma_datos, font=('Calibri', 13))
        self.pais.grid(row=6, column=1, padx=10, pady=5)
        self.pais.config(validate="key", validatecommand=(self.toma_datos.register(self.validate_input), '%P'))

        ##FECHA DE NACIMIENTO
        self.etiqueta_expdoc = Label(toma_datos, text='Fecha Expiracion Documento:')
        self.etiqueta_expdoc.grid(row=7, column=0)

        self.etiqueta_dia2 = Label(toma_datos, text='Dia:')
        self.etiqueta_dia2.grid(row=7, column=1, padx=0, pady=5)

        self.dia2 = Entry(toma_datos, font=('Calibri', 13), validate="key")
        self.dia2.grid(row=7,column=2, padx=5, pady=5)
        self.dia2.config(validatecommand=(self.toma_datos.register(self.validate_entry), '%P'))
        self.dia2.config(maxlength=2)

        self.etiqueta_mes2 = Label(toma_datos, text='Mes:')
        self.etiqueta_mes2.grid(row=7, column=3, padx=5, pady=5)

        self.mes2 = Entry(toma_datos, font=('Calibri', 13), validate="key")
        self.mes2.grid(row=7,column=4, padx=5, pady=5)
        self.mes2.config(validatecommand=(self.toma_datos.register(self.validate_entry), '%P'))
        self.mes2.config(maxlength=2)

        self.etiqueta_año2 = Label(toma_datos, text='Año:')
        self.etiqueta_año2.grid(row=7, column=5, padx=5, pady=5)

        self.año2 = Entry(toma_datos, font=('Calibri', 13), validate="key")
        self.año2.grid(row=7,column=6, padx=5, pady=5)
        self.año2.config(validatecommand=(self.toma_datos.register(self.validate_entry), '%P'))
        self.año2.config(maxlength=4)


        ##HABITACIONES
        self.etiqueta_habitacion = Label(toma_datos, text='Habitacion:')
        self.etiqueta_habitacion.grid(row=8, column=0)

        self.habitaciones = ['Habitaciones',301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316]
        self.habitacion = StringVar(toma_datos)
        self.habitacion.set(self.habitaciones[0])
        self.habitacionMenu = OptionMenu(toma_datos, self.habitacion, *self.habitaciones)
        self.habitacionMenu.grid(row=8, column=1, padx=10, pady=5)

        ##BOTON PARA GUARDAR LA RESERVA
        btn_guardar = Button(toma_datos, text="Guardar", width=10, font=('Calibri', 14, 'bold'),command=self.btn_guardar)
        btn_guardar.grid(row=9, column=0, pady=10)

        ##BOTON PARA SALIR AL MENU PRINCIPAL
        btn_salir = Button(toma_datos, text="Salir", width=10, font=('Calibri', 14, 'bold'), command=self.btn_salir)
        btn_salir.grid(row=9, column=1, pady=10)


    def btn_salir(self):
        self.ventana_check.destroy()

    def btn_guardar(self):
        tipodoc = self.opcion.get()
        numdoc = self.numdoc.get()
        dia = self.dia.get()
        mes = self.mes.get()
        año = self.año.get()
        fecExp = f"{dia}/{mes}/{año}"
        nombre = self.nombre.get()
        apelldio1 = self.apellido1.get()
        apellido2 = self.apellido2.get()
        pais = self.pais.get()
        dia2 = self.dia2.get()
        mes2 = self.mes2.get()
        año2 = self.año2.get()
        fecNac = f"{dia2}/{mes2}/{año2}"
        habitacion = self.habitacion.get()
        print(fecNac,":",fecExp)
        print(nombre)
        cli = cliente.Cliente(tipodoc,numdoc,fecExp,nombre,apelldio1,apellido2,pais,fecNac,habitacion)
        cli.registrarCliente()
        self.ventana_check.destroy()

    def validate_entry(self, input_text):
        if input_text.isdigit():
            return True
        elif input_text == "":
            return True
        else:
            return False


    def validate_input(self, input_text):
        if input_text.isalpha() or input_text == "":
            return True
        else:
            return False
