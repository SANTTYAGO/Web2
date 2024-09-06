# Proyecto de Tienda en Línea con Flask y SQLite

Este proyecto es una aplicación web de tienda en línea desarrollada con **Flask** y **SQLite**. Permite mostrar una lista de productos, visualizar detalles individuales de cada producto y proporciona una estructura de base de datos para almacenar la información de productos. La aplicación utiliza plantillas **Jinja** para generar contenido dinámico y se conecta a una base de datos **SQLite** para gestionar los productos.

## Características

- **Lista de productos**: Despliega una lista de productos con información como nombre, marca y precio.
- **Vista de producto individual**: Muestra detalles completos de cada producto, como su categoría, descripción, imagen y precio.
- **Navegación amigable**: Cada producto en la lista tiene un enlace que lleva a la página de detalles del producto.
- **Sistema de base de datos**: Se utiliza SQLite para gestionar los datos de los productos.

## Tecnologías

- **Backend**: Flask
- **Base de Datos**: SQLite
- **Lenguaje**: Python
- **Frontend**: HTML, CSS
- **Plantillas**: Jinja

## Estructura de Archivos

```bash
├── templates/
│   ├── base.html          # Plantilla base para todas las páginas
│   ├── index.html         # Página de inicio que muestra la lista de productos
│   └── producto.html      # Página de detalles de cada producto
├── static/
│   ├── css/
│   │   └── estilos.css    # Archivo de estilos CSS
│   └── imagenes/
│       └── logo.png       # Logotipo de la tienda
├── app.py                 # Archivo principal de la aplicación Flask
├── datos.py               # Script para gestionar y cargar los datos en SQLite
├── Web2.sqlite3           # Archivo de base de datos SQLite
```

## Instalación

1. Clona este repositorio.
2. Instala Flask si no lo tienes:
   ```bash
   pip install Flask
   ```
3. Asegúrate de que los datos de la base de datos están configurados correctamente en `Web2.sqlite3`. Si es necesario, puedes ejecutar el script `datos.py` para crear e insertar los productos.
4. Ejecuta la aplicación:
   ```bash
   python main.py
   ```
