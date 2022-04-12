#!/usr/bin/python3
"""Defines DBStorage engine """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from os import getenv
from models.base_model import Base, BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """ Represents a storage engine

    Attributes:
        - __engine: engine
        - __session: session """

    __engine = None
    __session = None

    def __init__(self):
        """ Initialize the storage engine """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(getenv("HBNB_MYSQL_USER"),
                                              getenv("HBNB_MYSQL_PWD"),
                                              getenv("HBNB_MYSQL_HOST"),
                                              getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return a dictionary of objects """
        if cls != None:
            objects = self.__session.query(type(cls))
        else:
            objects =  self.__session.query(User).all()
            objects +=  self.__session.query(State).all()
            objects +=  self.__session.query(City).all()
            objects +=  self.__session.query(Amenity).all()
            objects +=  self.__session.query(Place).all()
            objects +=  self.__session.query(Review).all()
        return {"{}.{}".format(type(obj).__name__, obj.id): obj for obj in objects}

    def new(self, obj): 
        """ Add the object to the current database session """
        self.__session.add(obj)

    def save(self): 
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None): 
        """ Delete from the current database session obj if not None """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables in the database """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

