from tkinter import ttk
from tkinter import *
import sqlite3


class VentanaPrincipal:
    db = 'database/productos.db'

    def __init__(self, root):
        self.ventana = root
        self.ventana.title("App Gestor de Productos")  # Titulo de la ventana
        self.ventana.resizable(1, 1)  # Activa la redimension de la ventana. Para desactivarla: (0,0)
        self.ventana.wm_iconbitmap('recursos/icon.ico')

        # Creacion del contenedor Frame principal
        frame = LabelFrame(self.ventana, text="Registrar un nuevo Producto",font=('Calibri', 16, 'bold')
)

        frame.grid(row=0, column=0, columnspan=3, pady=20)
        self.etiqueta_nombre = Label(frame, text="Nombre: ",font=('Calibri', 13))  # Etiqueta de texto ubicada en el frame
        self.etiqueta_nombre.grid(row=1, column=0)
        self.nombre = Entry(frame,font=('Calibri', 13))
        self.nombre.focus()
        self.nombre.grid(row=1, column=1)

        # Label Precio
        self.etiqueta_precio = Label(frame, text="Precio",font=('Calibri', 13))  # Etiqueta de texto ubicada en el frame
        self.etiqueta_precio.grid(row=2, column=0)

        # Entry precio ( caja de texto que recivira el precio)
        self.precio = Entry(frame,font=('Calibri', 13))
        self.precio.grid(row=2, column=1)

        # Boton añadir producto
        s = ttk.Style()
        s.configure('my.TButton', font=('Calibri', 14, 'bold'))
        self.boton_anadir = ttk.Button(frame, text="Guardar Producto", command=self.add_producto,style='my.TButton')
        self.boton_anadir.grid(row=3, columnspan=2, sticky=W + E)

        # Tabla de productos
        # Estilo personalizado para la tabla
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))
        style.configure("mystyle.Treeview.Heading",
                        font=('Calibri', 13, 'bold'))  # Se modifica la fuente de las cabeceras
        style.layout("mystyle.Treeview", [("mystyle.Treeview.treearea", {'sticky': 'nswe'})])  # Eliminamos los bordes

        # Estructura de la tabla
        self.tabla = ttk.Treeview(height=20, columns=2, style="mystyle.Treeview")
        self.tabla.grid(row=4, column=0, columnspan=2)
        self.tabla.heading('#0', text='Nombre', anchor=CENTER)  # Encabezado 0
        self.tabla.heading('#1', text='Precio', anchor=CENTER)  # Encabezado 1

        # Llamada al metodo get_productos() para obtener el listrado de productos al inicio de la app
        self.get_productos()

        # Mensaje informativo para el usuario
        self.mensaje = Label(text='', fg='red')
        self.mensaje.grid(row=3, column=0, columnspan=2, sticky=W + E)

        # Botones Eliminar y Editar
        s = ttk.Style()
        s.configure('my.TButton', font=('Calibri', 14, 'bold'))
        self.boton_eliminar = ttk.Button(text='ELIMINAR', command=self.del_producto,style='my.TButton')
        self.boton_eliminar.grid(row=5, column=0, sticky=W + E)
        self.boton_editar = ttk.Button(text='EDITAR', command=self.edit_producto,style='my.TButton')
        self.boton_editar.grid(row=5, column=1, sticky=W + E)

    def db_consulta(self, consulta, parametros=()):
        with sqlite3.connect(self.db) as con:  # Indicamos una conexcion con la base de datos (alias con)
            cursor = con.cursor()  # Generamos un cursor de la conexion para poder operar en la base de datos
            resultado = cursor.execute(consulta, parametros)  # Preparar la consulta SQL (con parametros si los hay)
            con.commit()  # Ejecuta la consulta SQL preparada anteriormente
        return resultado  # Retornar el resultado de la consulta SQL

    def get_productos(self):
        # Lo primero al iniciar la app vamos a limpiar la tabla por si hubiera datos residuales o antiguos
        registros_tabla = self.tabla.get_children()  # Obtener todos los datos de la tabla
        for fila in registros_tabla:
            self.tabla.delete(fila)
        # Consulta SQL
        query = 'SELECT * FROM producto ORDER BY nombre DESC'
        registros = self.db_consulta(query)  # Se hace la llamada al metodo db_consulta

        # Escribir los datos por pantalla
        for fila in registros:
            print(fila)
            self.tabla.insert('', 0, text=fila[1], values=fila[2])

        print(registros)  # Se muestran los resultados

    def validacion_nombre(self):
        return self.nombre.get().strip() != ""

    def validacion_precio(self):
        try:
            precio = float(self.precio.get())
            return precio > 0
        except ValueError:
            return False

    def add_producto(self):
        if not self.validacion_nombre():
            print("El nombre es obligatorio")
            self.mensaje['text'] = 'El nombre el obligatorio y no puede estar vacío'
            return
        if not self.validacion_precio():
            print("El precio es obligatorio")
            self.mensaje['text'] = 'El precio es obligatorio y debe ser un número válido mayor que 0'
            return

        query = 'INSERT INTO producto VALUES (null,?,?)'
        parametros = (self.nombre.get(), self.precio.get())
        self.db_consulta(query, parametros)
        print("Datos guardados")
        self.mensaje['text'] = 'Producto {} añadido con exito'.format(self.nombre.get())
        self.nombre.delete(0, END)
        self.precio.delete(0, END)
        self.get_productos()  # Cuando se finalice la inserción de datos volvemos a invocar a este método para actualizar el contenido

    def del_producto(self):
        self.mensaje['text'] = ''
        try:
            self.tabla.item(self.tabla.selection())['text'][0]
        except IndexError as e:
            self.mensaje['text'] = 'Por favor, seleccione un producto'
            return
        self.mensaje['text'] = ''
        nombre = self.tabla.item(self.tabla.selection())['text']
        query = 'DELETE FROM producto WHERE nombre = ?'
        self.db_consulta(query, (nombre,))  # Ejecutar la consulta
        self.mensaje['text'] = 'Producto {} eliminado con éxito'.format(nombre)
        self.get_productos()

    def edit_producto(self):
        try:
            nombre = self.tabla.item(self.tabla.selection())['text']
            precio = self.tabla.item(self.tabla.selection())['values'][0]
            VentanaEditarProducto(self, nombre, precio, self.mensaje)
        except IndexError:
            self.mensaje['text'] = 'Por favor, seleccione un produco'


class VentanaEditarProducto():

    def __init__(self, ventana_principal, nombre, precio, mensaje):
        self.ventana_principal = ventana_principal
        self.nombre = nombre
        self.precio = precio
        self.mensaje = mensaje

        self.ventana_editar = Toplevel()
        self.ventana_editar.title("Editar Producto")

        # Creacion del contenedor Frame para la edición del producto
        frame_ep = LabelFrame(self.ventana_editar, text="Editar el siguiente Producto", font=('Calibri', 16, 'bold'))
        frame_ep.grid(row=0, column=0, columnspan=2, pady=20, padx=20)

        # Label y Entry para el nombre antiguo (solo lectura)
        Label(frame_ep, text="Nombre antiguo: ", font=('Calibri', 13)).grid(row=1, column=0)
        Entry(frame_ep, textvariable=StringVar(self.ventana_editar, value=nombre), state='readonly', font=('Calibri', 13)).grid(row=1, column=1)

        # Label y Entry para el Nombre nuevo
        Label(frame_ep, text="Nombre nuevo: ", font=('Calibri', 13)).grid(row=2, column=0)
        self.input_nombre_nuevo = Entry(frame_ep, font=('Calibri', 13))
        self.input_nombre_nuevo.grid(row=2, column=1)
        self.input_nombre_nuevo.focus()

        # Precio antiguo (solo lectura)
        Label(frame_ep, text="Precio antiguo: ", font=('Calibri', 13)).grid(row=3, column=0)
        Entry(frame_ep, textvariable=StringVar(self.ventana_editar, value=precio), state='readonly', font=('Calibri', 13)).grid(row=3, column=1)


        # Precio nuevo
        Label(frame_ep, text="Precio nuevo: ", font=('Calibri', 13)).grid(row=4, column=0)
        self.input_precio_nuevo = Entry(frame_ep, font=('Calibri', 13))
        self.input_precio_nuevo.grid(row=4, column=1)

        # Boton Actualizar Producto
        ttk.Style().configure('my.TButton', font=('Calibri', 14, 'bold'))

        # Ejemplo de como creamos y configuramos el estilo en una sola línea
        ttk.Button(frame_ep, text='Actualizar Producto', style='my.TButton', command=self.actualizar).grid(row=5, columnspan=2, sticky=W + E)

    def actualizar(self):
        nuevo_nombre = self.input_nombre_nuevo.get() or self.nombre
        nuevo_precio = self.input_precio_nuevo.get() or self.precio

        if nuevo_nombre and nuevo_precio:
            query = 'UPDATE producto SET nombre = ?, precio = ? WHERE nombre = ?'
            parametros = (nuevo_nombre, nuevo_precio, self.nombre)
            self.ventana_principal.db_consulta(query, parametros)
            self.mensaje['text'] = 'El producto {} ha sido actualizado con éxito'.format(self.nombre)
        else:
            self.mensaje['text'] = 'No se pudo actualizar el producto {self.nombnre}'

        self.ventana_editar.destroy()
        self.ventana_principal.get_productos()


if __name__ == '__main__':
    root = Tk()  # Instancia de la ventana principal
    app = VentanaPrincipal(root)  # Se envia a la clase VentanaPrincipal el control sobre la ventana root
    root.mainloop()  # Comenzamos el bicle de aplicacion, es como un while True
