import sqlite3
from tkinter import *



class BuscaCliente:

    def __init__(self, ventana_inicio):
        self.ventana_inicio = ventana_inicio
        self.ventana_busca = Toplevel()
        self.ventana_busca.title("Hostal Cruz Sol")
        self.ventana_busca.resizable(1, 1)
        self.ventana_busca.wm_iconbitmap('recursos/cruzSol.ico')
        self.ventana_busca.geometry("1300x600+240+120")

        self.opciones = ['DNI', 'NIF', 'PASAPORTE']

        titulo = Label(self.ventana_busca, text="BUSCAR CLIENTE", font=('Calibri', 16, 'bold'), fg='#000080')
        titulo.grid(row=0,column=0)

        self.frame_busqueda = LabelFrame(self.ventana_busca, text="Busqueda de clientes",font=('Calibri', 16, 'bold'))
        self.frame_busqueda.grid(row=1,column=0)

        self.etiqueta_tipo = Label(self.frame_busqueda, text='Tipo Documento:')
        self.etiqueta_tipo.grid(row=0, column=0)

        self.opcion = StringVar(self.frame_busqueda)
        self.opcion.set(self.opciones[0])
        self.opcionMenu = OptionMenu(self.frame_busqueda, self.opcion, *self.opciones)
        self.opcionMenu.grid(row=1, column=0, padx=10, pady=5)

        self.numdoc = Entry(self.frame_busqueda, font=('Calibri', 13))
        self.numdoc.grid(row=1, column=1, padx=5, pady=5)

        self.etiqueta_nombre = Label(self.frame_busqueda, text="Nombre:", font=('Calibri', 11))
        self.etiqueta_nombre.grid(row=2, column=0)

        self.nombre = Entry(self.frame_busqueda)
        self.nombre.grid(row=2,column=1, pady=5, padx=2)

        self.btn_buscar = Button(self.frame_busqueda, text="Buscar", width=10, font=('Calibri', 14, 'bold'),command=self.listarClientes)
        self.btn_buscar.grid(row=3,column=1, pady=5)

        self.btn_salir = Button(self.frame_busqueda, text="Salir", width=10, font=('Calibri', 14, 'bold'),command=self.btn_salir)
        self.btn_salir.grid(row=3,column=0, pady=5)

        ##  LISTA DE LOS CLIENTES ENCONTRADOS   #########################################
        self.frame_clientes = LabelFrame(self.ventana_busca, text="Clientes encontrados",font=('Calibri', 16, 'bold'), width=1000,padx=60, pady=20)
        self.frame_clientes.grid(row=1,column=1, pady=5, padx=15)
        self.frame_clientes.anchor('n')

        self.documento_cliente = Label(self.frame_clientes, text="Documento", font=('Calibri', 11, 'bold'))
        self.documento_cliente.grid(row=1, column=0, padx=15)

        self.nombre_cliente = Label(self.frame_clientes, text="Nombre", font=('Calibri', 11, 'bold'))
        self.nombre_cliente.grid(row=1, column=1, padx=15)

        self.apellidos_cliente = Label(self.frame_clientes, text="Apellidos", font=('Clibri', 11, 'bold'))
        self.apellidos_cliente.grid(row=1, column=2, padx=15)

        self.pais_cliente = Label(self.frame_clientes, text="Pais", font=('Calibri', 11, 'bold'))
        self.pais_cliente.grid(row=1, column=3, padx=15)

        ##  AQUI SE DEBERIAN DE LISTAR LOS CLIENTES ####################################

        self.documento_cliente_encontrado = Label(self.frame_clientes, text="", font=('Calibri', 11))
        self.documento_cliente_encontrado.grid(row=3, column=0, padx=15)

        self.nombre_cliente_encontrado = Label(self.frame_clientes, text="", font=('Calibri', 11))
        self.nombre_cliente_encontrado.grid(row=3, column=1, padx=15)

        self.apellidos_cliente_encontrado = Label(self.frame_clientes, text="", font=('Calibri', 11))
        self.apellidos_cliente_encontrado.grid(row=3, column=2, padx=15)

        self.pais_cliente_encontrado = Label(self.frame_clientes, text="", font=('Calibri', 11))
        self.pais_cliente_encontrado.grid(row=3, column=3, padx=15)



    def busquedaClientes(self):
        tipoDoc = self.opcion.get()
        numDoc = self.numdoc.get()
        nombre = self.nombre.get()

        conexion = sqlite3.connect('database/usuarios.db')
        cursor = conexion.cursor()

        if(numDoc == ""):
            cursor.execute('SELECT documento, numeroDoc, nombre, apellido1, apellido2, fecNac FROM clientesPER WHERE nombre LIKE ?', (nombre + '%',))
        elif (nombre == ""):
            cursor.execute('SELECT documento, numeroDoc, nombre, apellido1, apellido2, fecNac FROM clientesPER WHERE documento = ? AND numeroDoc = ?', (tipoDoc,numDoc))

        clientes = cursor.fetchall()
        conexion.close()

        return clientes


    def listarClientes(self):

        clientes = self.busquedaClientes()

        for i, cliente in enumerate(clientes, start=2):
            documento = f"{cliente[0]} {cliente[1]}"
            nombre = cliente[2]
            apellidos = f"{cliente[3]} {cliente[4]}"
            pais = cliente[5]

            documento_encontrado = Label(self.frame_clientes, text=documento, font=('Calibri', 11))
            documento_encontrado.grid(row=i,column=0)

            nombre_encontrado = Label(self.frame_clientes, text=nombre, font=('Calibri', 11))
            nombre_encontrado.grid(row=i,column=1)

            apellidos_encontrado = Label(self.frame_clientes, text=apellidos, font=('Calibri',11))
            apellidos_encontrado.grid(row=i, column=2)

            pais_encontrado = Label(self.frame_clientes, text=pais, font=('Calibri', 11))
            pais_encontrado.grid(row=i, column=3)

            self.documento_cliente_encontrado = documento
            self.nombre_cliente_encontrado = nombre
            self.apellidos_cliente_encontrado = apellidos
            self.pais_cliente_encontrado = pais

    def btn_salir(self):
        self.ventana_busca.destroy()




