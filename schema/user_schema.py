from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    #Como queremos que se estructuren los datos que nos mandan desde el cliente al servidor
    id: Optional[str]
    name: str
    username: str
    user_password: str
    
class DataUser(BaseModel):
    username: str
    user_password: str