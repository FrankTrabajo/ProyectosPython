from tkinter import ttk
from tkinter import *
from tkinter import Tk, Label, LabelFrame, Entry, PhotoImage, Canvas
import sqlite3
import usuario

class VentanaRegistro:

    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        self.ventanaRegistro = Toplevel()
        self.ventanaRegistro.title("Hostal Cruz Sol")
        self.ventanaRegistro.wm_iconbitmap('recursos/cruzSol.ico')
        self.ventanaRegistro.geometry("500x200+240+120")

        # Creacion del contenedor Frame para registrar nuevo ususario
        frame_ep = LabelFrame(self.ventanaRegistro, text="Registrar nuevo usuario", font=('Calibri', 16, 'bold'), borderwidth=0)
        frame_ep.pack()

        self.etiqueta_nombre = Label(frame_ep, text="Nombre: ", font=('Calibri', 13))  # Etiqueta de texto ubicada en el frame
        self.etiqueta_nombre.grid(row=1, column=0)

        self.nombre = Entry(frame_ep, font=('Calibri', 13))
        self.nombre.grid(row=1, column=1, padx=10, pady=5)
        self.nombre.focus()

        self.etiqueta_apellido = Label(frame_ep, text="Apellido: ", font=('Calibri', 13))  # Etiqueta de texto ubicada en el frame
        self.etiqueta_apellido.grid(row=2, column=0)

        self.apellido = Entry(frame_ep, font=('Calibri', 13))
        self.apellido.grid(row=2, column=1, padx=10, pady=5)

        self.etiqueta_contraseña = Label(frame_ep, text="Contraseña: ", font=('Calibri', 13))  # Etiqueta de texto ubicada en el frame
        self.etiqueta_contraseña.grid(row=3, column=0, padx=10, pady=5)

        self.contraseña = Entry(frame_ep, font=('Calibri', 13), show='*')
        self.contraseña.grid(row=3, column=1)

        self.mensaje = Label(frame_ep, text='', fg='red')
        self.mensaje.grid(row=4, column=0, columnspan=2, sticky=W + E)

        self.btn_sesion = Button(frame_ep, text="Registrar", borderwidth=0, bg='#ABB9D8', command=self.registrarUsuario)
        self.btn_sesion.grid(row=2, column=2, pady=10, padx=50)

        self.atras = Button(frame_ep, text="Atrás", borderwidth=0, bg='#ABB9D8', command=self.volver)
        self.atras.grid(row=3, column=2, pady=10, padx=50)

    def volver(self):
        self.ventanaRegistro.destroy()

    def registrarUsuario(self):
        nombre = self.nombre.get()
        apellido = self.apellido.get()
        contraseña = self.contraseña.get()

        # Verificar si los campos están vacíos
        if not nombre or not apellido or not contraseña:
            self.mensaje['text'] = "Por favor, complete todos los campos."
            return

        try:
            u1 = usuario.Usuario(nombre, apellido, contraseña)
            u1.registrarUsuario()
            self.ventanaRegistro.destroy()
        except Exception as e:
            print("Ha ocurrido un problema:", e)

