#!/usr/bin/python3
"""
Tests base model
"""

import os
import re
import json
import uuid
import unittest
from time import sleep
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Tests atributes of base model
    """

    def setUp(self):
        """
        setup test
        """
        pass

    def test_basic(self):
        """
        tests basic inputs
        """
        my_model = BaseModel()
        my_model.name = "ALX"
        my_model.number = 89
        self.assertEqual([my_model.name, my_model.number],
                            ["ALX", 89])

    def test_datetime(self):
        """
        tests datetime
        """
        pass

if __name__== '__main__':
    unittest.main()

