#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """This class defines a city by various attributes"""

    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)

    # Relationship with Place
    places = relationship("Place", cascade="all, delete", backref="cities")

