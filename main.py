from flask import Flask, render_template, redirect
import sqlite3

# Cargar los Datos
Conexion = sqlite3.connect('Web2.sqlite3')
Conexion.row_factory = sqlite3.Row # Modo Diccionario
Cursor = Conexion.cursor()
Cursor.execute("""
    SELECT * FROM productos;
""")
productos = [ dict(producto) for producto in Cursor.fetchall() ]
Cursor.close()
Conexion.close()

# Aplicacion
app = Flask(__name__)

# Rutas
@app.route('/')
def ruta_raiz():
    return render_template('index.html', productos=productos)

@app.route('/producto/<int:pid>')
def ruta_producto(pid):
    for producto in productos:
        if pid == producto['id']:
            return render_template('producto.html', producto=producto)
    return redirect('/')

# Programa Principal
if __name__== '__main__':
    app.run(host='0.0.0.0', debug=True)
    