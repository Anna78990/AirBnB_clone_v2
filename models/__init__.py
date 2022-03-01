#!/usr/bin/python3
"""Link BaseModel to FileStorage by using variable storage"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
