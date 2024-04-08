from flask import Flask, render_template, request, redirect, url_for
import db
from models import Tarea # Importamos la clase tarea desde models.py
app = Flask(__name__) # En app se encuentra nuestro servidor web de Flask

@app.route('/')
def home():
    todas_las_tareas = db.session.query(Tarea).all() # Consulta y almacena todas las tareas de la base de datos
    return render_template("index.html", lista_de_tareas=todas_las_tareas) # Se carga el template de index

@app.route('/crear-tarea', methods=['POST'])
def crear():
    tarea = Tarea(contenido=request.form['contenido_tarea'], hecha=False)
    db.session.add(tarea)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/eliminar-tarea/<id>')
def eliminar(id):
    tarea = db.session.query(Tarea).filter_by(id=int(id)).delete() #Se busca dentro de la base de datos, aquel registro cuyo id coincida con el aportado por el parametro de la ruta
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/tarea-hecha/<id>')
def hecha(id):
    tarea = db.session.query(Tarea).filter_by(id=int(id)).first() # Se obtiene la tarea que se busca
    tarea.hecha = not(tarea.hecha) # Guardamos en la variable booleana de la tarea su contrario, Si es False pues True
    db.session.commit()
    return redirect(url_for('home'))



if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine) #Creamos el modelo de datos
    app.run(debug=True) # El debug=True hace que cada vez que reiniciemos el servidor o modifiquemos codigo, el servidor de Flask se reinicie solo



