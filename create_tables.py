#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# Update the database URL as per your setup
DATABASE_URL = "mysql+mysqldb://hbnb_test:hbnb_test_pwd@localhost/hbnb_test_db"

# Create an engine
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Create all tables
Base.metadata.create_all(engine)

