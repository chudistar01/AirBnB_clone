#!/bin/usr/python3
"""
modules init
"""
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
