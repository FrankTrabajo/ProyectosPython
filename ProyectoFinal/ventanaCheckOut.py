from tkinter import *
from tkinter import Label, LabelFrame, Entry
from tkcalendar import Calendar
import sqlite3
import cliente
import ventanaInicio
class CheckOut:

    def __init__ (self, ventana_inicio):
        self.ventana_inicio = ventana_inicio
        self.ventana_reserva = Toplevel()
        self.ventana_reserva.title("Hostal Cruz Sol")
        self.ventana_reserva.resizable(1, 1)  # Activa la redimension de la ventana. Para desactivarla (0,0)
        self.ventana_reserva.wm_iconbitmap('recursos/cruzSol.ico')
        self.ventana_reserva.geometry("1065x450+240+120")

        # Obtener y guardar los clientes desde la base de datos
        self.clientes = self.obtener_clientes_desde_bd()

        # Llamar a listar_clientes para mostrar los clientes
        self.listar_clientes()

        titulo = Label(self.ventana_reserva, text="CHECKOUT", font=('Calibri', 16, 'bold'), fg='#000080')
        titulo.grid(row=0, column=0)

        clientes_out = LabelFrame(self.ventana_reserva, text="CLIENTES", font=('Calibri', 16, 'bold'))
        clientes_out.grid(row=1, column=0, padx=10)


    def listar_clientes(self):

        for widget in self.ventana_reserva.winfo_children():
            widget.destroy()

        # Etiquetas de encabezado
        self.etiqueta_doc_cli = Label(self.ventana_reserva, text="Documento", padx=55, pady=5, font=('Calibri', 11, 'bold'))
        self.etiqueta_doc_cli.grid(row=0, column=0)

        self.etiqueta_nombre_cli = Label(self.ventana_reserva, text="Nombre", padx=55, pady=5, font=('Calibri', 11, 'bold'))
        self.etiqueta_nombre_cli.grid(row=0, column=1)

        self.etiqueta_apellido_cli = Label(self.ventana_reserva, text="Apellidos", padx=55, pady=5, font=('Calibri', 11, 'bold'))
        self.etiqueta_apellido_cli.grid(row=0, column=2)

        self.etiqueta_hab_cli = Label(self.ventana_reserva, text="Habitacion", padx=55, pady=5, font=('Calibri', 11, 'bold'))
        self.etiqueta_hab_cli.grid(row=0, column=3)

        # Actualizar las etiquetas con los datos y color verde
        for i, cliente in enumerate(self.clientes, start=2):
            id_cliente = cliente[1]
            documento = f"{cliente[0]} {cliente[1]}"
            nombre = cliente[2]
            apellidos = f"{cliente[3]} {cliente[4]}"
            habitacion = cliente[5]

            # Actualizar las etiquetas
            doc_cli = Label(self.ventana_reserva, text=documento, padx=55, pady=5, font=('Calibri', 11))
            doc_cli.grid(row=i, column=0)

            nombre_cli = Label(self.ventana_reserva, text=nombre, padx=55, pady=5, font=('Calibri', 11))
            nombre_cli.grid(row=i, column=1)

            apellido_cli = Label(self.ventana_reserva, text=apellidos, padx=55, pady=5, font=('Calibri', 11))
            apellido_cli.grid(row=i, column=2)

            hab_cli = Label(self.ventana_reserva, text=habitacion, padx=55, pady=5, font=('Calibri', 11))
            hab_cli.grid(row=i, column=3)

            eliminar_funcion = lambda id_cliente=id_cliente, habitacion=habitacion: self.eliminarCliente(id_cliente, habitacion)

            btn_elim = Button(self.ventana_reserva, text="Check Out", padx=55, pady=5, font=('Calibri', 11), command=eliminar_funcion)
            btn_elim.grid(row=i, column=4)

    def obtener_clientes_desde_bd(self):
        # Establecer conexión a la base de datos
        conn = sqlite3.connect('database/usuarios.db')
        cursor = conn.cursor()

        # Ejecutar la consulta para obtener los clientes
        cursor.execute("SELECT documento, numeroDoc, nombre, apellido1, apellido2, habitacion FROM clientesTEMP")
        clientes = cursor.fetchall()

        # Cerrar la conexión
        conn.close()

        return clientes

    def eliminarCliente(self, idCliente, numHab):
        conexion = sqlite3.connect('database/usuarios.db')
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM clientesTEMP WHERE numeroDoc = ?", (idCliente,))
        cursor.execute("UPDATE habitacion SET ocupada = 0 WHERE numeroHab = ?", (numHab,))
        conexion.commit()
        conexion.close()

        # Volver a obtener los clientes desde la base de datos y actualizar la lista
        self.clientes = self.obtener_clientes_desde_bd()
        self.listar_clientes()

        # Llamar al método de ventanaInicio para actualizar la lista
        self.ventana_inicio.actualizar_lista_clientes()
