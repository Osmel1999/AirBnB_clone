#!/usr/bin/python3
"""
A class User that inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    This class allows to create
    states in the application.
    User Class attributes
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
