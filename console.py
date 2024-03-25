#!/usr/bin/python3
"""
The console
"""

import cmd
import json
import re
import models
from models.base_model import BaseModel

class HBHBCommand(cmd.Cmd):
    """
    console class
    """

    prompt = '(hbnb)'

    def do_emptyline(self, line):
        """
        overwrites empty lines
        """
        return False

    def do_quit(self, line):
        """
        handles the quit command
        """
        return True

    def do_EOF(self, line):
        """
        handles end of line
        """
        return True
