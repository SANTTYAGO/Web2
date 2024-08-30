# importar la libreria para gestionar la DB
import sqlite3

# Establecer la Conexion
conexion =  sqlite3.connect('Web2.sqlite3')
cursor = conexion.cursor()

# Eliminar la Tabla
cursor.execute("""
DROP TABLE IF EXISTS productos 
""")

# Crear la Tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY,
    categoria TEXT NOT NULL,
    marca TEXT NOT NULL,
    nombre TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    precio INTEGER NOT NULL
);
""")

# Insertar los Datos Iniciales
datos = [
    (1, 'Laptop', 'Dell', 'XPS 13', 'Laptop ultradelgada con pantalla de 13.3 pulgadas', 1200),
    (2, 'Laptop', 'HP', 'Spectre x360', 'Laptop convertible con pantalla táctil de 13.3 pulgadas', 1300),
    (3, 'Smartphone', 'Apple', 'iPhone 14', 'Smartphone con pantalla de 6.1 pulgadas y cámara avanzada', 999),
    (4, 'Smartphone', 'Samsung', 'Galaxy S23', 'Smartphone con pantalla de 6.2 pulgadas y batería de larga duración', 950),
    (5, 'Tablet', 'Apple', 'iPad Pro', 'Tablet de 11 pulgadas con procesador M1', 800),
    (6, 'Tablet', 'Samsung', 'Galaxy Tab S8', 'Tablet con pantalla de 11 pulgadas y S Pen incluido', 750),
    (7, 'Monitor', 'LG', 'UltraGear', 'Monitor de 27 pulgadas con tasa de refresco de 144Hz', 400),
    (8, 'Monitor', 'Dell', 'UltraSharp', 'Monitor de 27 pulgadas con resolución 4K', 500),
    (9, 'Auriculares', 'Sony', 'WH-1000XM4', 'Auriculares inalámbricos con cancelación de ruido', 350),
    (10, 'Auriculares', 'Bose', 'QuietComfort 35 II', 'Auriculares inalámbricos con cancelación de ruido y control de voz', 300),
]

# Cada uno de los Datos haga un insert
cursor.executemany("""
INSERT INTO productos VALUES (?, ?, ?, ?, ?, ?);
""", datos)

# Grabar
conexion.commit()
conexion.close()