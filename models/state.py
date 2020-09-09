#!/usr/bin/python3
"""
This module defines class State that inherits from BaseModel
"""
from models.base_model import BaseModel, Base
import models
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """
    Initialize class State with attribute
        name: (str) name of the state
    """
    __tablename__ = "states"
    name = Column(String(128), nullable="False")
    cities = relationship("City", cascade="all, delete", backref="state")

    @property
    def cities(self):
        """Return the list of cities"""
        return [city for city in models.storage.all(City).values() if
                self.id == city.state_id]
