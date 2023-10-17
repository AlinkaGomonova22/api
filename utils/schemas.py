import uuid
from dataclasses import dataclass


@dataclass  #какие данные будет содержать
class Users:
    id: int
    username: str
    password: str
    role: str
    age: int


# print(uuid.uuid4())