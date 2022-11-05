from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_200_OK
from schema.user_schema import UserSchema, DataUser
#from config.db import conn
from config.db import engine
from model.users import users
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List
import jwt as _jwt

_JWT_SECRET = "frrosoporte"

user = APIRouter()

@user.get("/")
def root():
    return {
        "message": "Hola Mundo"
    }
    
@user.get("/api/user", response_model=List[UserSchema])
def get_users():
    with engine.connect() as conn:
        result = conn.execute(users.select()).fetchall()
        
        return result
    
@user.get("/api/user/{user_id}", response_model=UserSchema)
def get_user(user_id: str):
    with engine.connect() as conn:
        #users.c indica que hacemos referencia a una columna, en este caso id
        result = conn.execute(users.select().where(users.c.id == user_id)).first()
        
        return result
    

@user.post("/api/user", status_code=HTTP_201_CREATED)
#Para estos datos data_user necesito crearlos en schema
def create_user(data_user: UserSchema):
    #with asegura que se abra y cierre la conexión a la BD
    with engine.connect() as conn:
        new_user = data_user.dict()
        new_user["user_password"] = generate_password_hash(data_user.user_password, "pbkdf2:sha256:30", 30)
        conn.execute(users.insert().values(new_user))
        
        return Response(status_code=HTTP_201_CREATED)
    
@user.post("/api/user/login", status_code=HTTP_200_OK)
def user_login(data_user: DataUser):
    with engine.connect() as conn:
        result = conn.execute(users.select().where(users.c.username == data_user.username).where()).first()

        if result != None:
            check_password = check_password_hash(result[3], data_user.user_password)
            if check_password:
                datos = {
                    "nombre": result[2],
                    "username": result[3],
                }
                token = _jwt.encode(datos, _JWT_SECRET)
                return {
                    "status": 200,
                    "mensaje": "Logueado correctamente",
                    "token": token,
                }
            else:
                return {
                    "status": 404,
                    "mensaje": "Datos incorrectos"
                }
    
@user.put("/api/user/{user_id}", response_model=UserSchema)
def update_user(data_update: UserSchema, user_id: str):
    with engine.connect() as conn:
        update_data["id"] = user_id
        update_data = data_update.dict()
        update_data["user_password"] = generate_password_hash(data_update.user_password, "pbkdf2:sha256:30", 30)
        conn.execute(users.update().values(update_data).where(users.c.id == user_id))
        
        result = conn.execute(users.select().where(users.c.id == user_id)).first()
        return result
    
@user.delete("/api/user/{user_id}", status_code=HTTP_204_NO_CONTENT)
def delete_user(user_id: str):
    with engine.connect() as conn:
        conn.execute(users.delete().where(users.c.id == user_id))
        
        return Response(status_code=HTTP_204_NO_CONTENT)