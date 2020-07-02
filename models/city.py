#!/usr/bin/python3
"""
Module that inherit from BaseModel class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City public Class attributes
    """
    state_id = ""
    name = ""
