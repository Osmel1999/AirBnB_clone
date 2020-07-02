#!/usr/bin/python3
"""
Module that inherit from BaseModel class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review public Class attributes
    """
    place_id = ""
    user_id = ""
    text = ""
