import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:
    """Datebase stroage engine for MySQl Using SQLAlchemy"""
    __engine = None
    __session = None

    def __init__(self):
        """instantiate a DBStorage object"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv('HBNB_MYSQL_USER'),
            os.getenv('HBNB_MYSQL_PWD'),
            os.getenv('HBNB_MYSQL_HOST'),
            os.getenv('HBNB_MYSQL_DB')), pool_pre_ping = True)
        
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Quary all object of of class or all object of no class is specified"""
        if cls:
            objs = self.__session.query(cls).all()
        else:
            objs = self.__session.query(State).all() + \
                   self.__session.query(City).all()
        return{"{}.{}".format(type(obj).__name__,obj.id): obj for obj in objs}  #list compheersion here
    
    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete the object from the current database session if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload the session from the database"""
        from models.state import State
        from models.city import City
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()