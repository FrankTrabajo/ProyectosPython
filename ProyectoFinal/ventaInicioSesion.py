from tkinter import ttk
from tkinter import *
from tkinter import Tk, Label, LabelFrame, Entry, PhotoImage, Canvas
import sqlite3

import main
import usuario
import ventanaInicio
import ventanaResgistro


class VentanaPrincipal:
    # Esta será la ventana principal que será la de inicio de sesión

    def __init__(self, ventana_sesion):
        self.ventana_sesion = ventana_sesion
        self.ventana = Toplevel()
        self.ventana.title("Hostal Cruz Sol")  # El título de la ventana
        self.ventana.resizable(1, 1)  # Activa la redimension de la ventana. Para desactivarla (0,0)
        self.ventana.wm_iconbitmap('recursos/cruzSol.ico')
        self.ventana.geometry("400x600+240+120")

        # Creacion del contenedor Frame principal
        titulo = Label(self.ventana, text="INICIO DE SESION", font=('Calibri', 16, 'bold'), fg='#000080')
        titulo.pack()

        # Creación de un contenedor Canvas para la imagen
        canvas_frame = LabelFrame(self.ventana, text="", font=('Calibri', 16, 'bold'), padx=20, pady=20, borderwidth=0)
        canvas_frame.pack()

        # Carga de la imagen
        self.filename = PhotoImage(file='recursos/cruzSol.png')
        canvas = Canvas(canvas_frame, width=400, height=100)
        canvas.create_image(110, 0, anchor='nw', image=self.filename)
        canvas.pack()

        frame = LabelFrame(self.ventana, text="", font=('Calibri', 16, 'bold'), padx=20, pady=20)
        frame.pack()

        self.etiqueta_nombre = Label(frame, text="Nombre: ", font=('Calibri', 13))  # Etiqueta de texto ubicada en el frame
        self.etiqueta_nombre.grid(row=1, column=0)

        self.nombre = Entry(frame, font=('Calibri', 13))
        self.nombre.grid(row=1, column=1)
        self.nombre.focus()

        self.etiqueta_contraseña = Label(frame, text="Contraseña: ", font=('Calibri', 13))  # Etiqueta de texto ubicada en el frame
        self.etiqueta_contraseña.grid(row=2, column=0, padx=10, pady=10)

        self.contraseña = Entry(frame, font=('Calibri', 13), show='*')
        self.contraseña.grid(row=2, column=1)

        self.mensaje = Label(frame, text='', fg='red')
        self.mensaje.grid(row=3, column=0, columnspan=2, sticky=W + E)

        self.btn_sesion = Button(frame, text="Iniciar sesión", borderwidth=0, bg='#ABB9D8', command=self.on_button_click)
        self.btn_sesion.grid(row=4, column=1, pady=10, padx=15)

        # Frame para crearse una cuenta nueva
        alta = LabelFrame(self.ventana, text="¿No tienes cuenta? Date de alta", font=('Calibri', 12, 'bold'), padx=20, pady=20)
        alta.pack()

        self.btn_sesion = Button(alta, text="Nuevo usuario", borderwidth=0, bg='#ABB9D8', command=self.botonRegistro)
        self.btn_sesion.grid(row=1, column=2, pady=10, padx=50)

    def on_button_click(self):
        self.inicioSesion()

    def botonRegistro(self):
        try:
            self.registro = ventanaResgistro
            self.registro.VentanaRegistro(self)
        except IndexError:
            print("Ha habido un problema")

    def inicioSesion(self):
        conexion = sqlite3.connect('database/usuarios.db')
        cursor = conexion.cursor()

        # Consulta para obtener nombre y tipo de usuario
        cursor.execute('SELECT nombre, tipo FROM usuario WHERE nombre = ? AND contraseña = ?', (self.nombre.get(), self.contraseña.get()))
        usuario = cursor.fetchone()

        nombre = self.nombre.get()
        contraseña = self.contraseña.get()

        # Verificar si los campos están vacíos
        if not nombre or not contraseña:
            self.mensaje['text'] = "Por favor, complete todos los campos."
            return

        if usuario:
            nombre, tipo = usuario
            if tipo == 'ADMIN':
                self.mensaje_admin = "Bienvenido", nombre, "Administrador"
                self.abrirIncio()
                self.ventana.destroy()
            else:
                self.mensaje_empleado = "Bienvenido", nombre, "Empleado"
                self.abrirIncio()
                self.ventana.destroy()
        else:
            print("Usuario incorrecto o no existe")
            self.nombre.delete(0, 'end')
            self.contraseña.delete(0, 'end')

        conexion.close()


    def abrirIncio(self):
        self.inicio = ventanaInicio.VentanaInicio(self)

