from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from sqlalchemy import Column, String

class User(BaseModel):
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship('Place', backref='user', cascade='all, delete-orphan')
