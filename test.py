#!/usr/bin/python3
from datetime import datetime
import time
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.user import User
import io
from models.engine.db_storage import DBStorage
console = __import__('console').HBNBCommand


con = console()
arg = 'State name="Arizona"'
cr = str(con.do_create(arg))
with open('file.json') as f:
    contents = f.read()
f.close()
print('"name": "Arizona"' in contents)
u = User(name="")
storage = DBStorage()
print(storage)
print(storage.all('State'))
