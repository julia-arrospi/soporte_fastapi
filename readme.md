# Para ver la documentación autogenerada de Swagger:
http://127.0.0.1:8000/docs

## Para correr el entorno virtual

.\venv\Scripts\activate

o 

.\venv\Scripts\activate.bat   

# Requerimientos, estan dentro del entorno virtual venv

pip install uvicorn
pip install fastapi
pip install sqlalchemy
pip install pymysql
pip install cryptography

pip freeze > requirements.txt, hace un dump de los requerimientos en un archivo.

# Para correr la app:

uvicorn main:app --reload

# Descripcion de carpetas
- Config --> Config de la BBDD
- Schema --> Esquema de usuarios
- Model --> Esquema de las tablas
- Router --> Rutas de la aplicacion




