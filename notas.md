# Para ver la documentación autogenerada de Swagger:
http://127.0.0.1:8000/docs

## Para correr el entorno virtual
*win*
`.\venv\Scripts\activate`

o 
*linux*
`.\venv\Scripts\activate.bat`

## Requerimientos, estan dentro del entorno virtual venv

pip install uvicorn
pip install fastapi
pip install sqlalchemy
pip install pymysql
pip install cryptography
*estos son algunos de los requerimientos, los dumpeamos en un archivo requirements.txt para instalarlos todos juntos*

`pip freeze > requirements.txt` hace un dump de los requerimientos en un archivo.

`pip install -r requirements.txt` instala todas las dependencias.

# Para correr la app:

`uvicorn main:app --reload`

# Descripcion de carpetas
- Config --> Config de la BBDD
- Schema --> Esquema de usuarios
- Model --> Esquema de las tablas
- Router --> Rutas de la aplicacion