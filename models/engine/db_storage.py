#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session


username = getenv("HBNB_MYSQL_USER")
password = getenv("HBNB_MYSQL_PWD")
host = getenv("HBNB_MYSQL_HOST")
db = getenv("HBNB_MYSQL_DB")
dev_env = getenv("HBNB_ENV")
classes = {"State": State, "City": City, "User": User,
           "Place": Place, "Review": Review, "Amenity": Amenity}


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(username,
                                              password,
                                              host,
                                              db),
                                      pool_pre_ping=True)

        if dev_env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries on the current database"""
        objs = {}
        if cls is not None and cls in classes:
            for obj in self.__session.query(classes[cls]).all():
                key = str(obj.__class__.__name__) + "." + str(obj.id)
                objs[key] = obj
        else:
            for key, val in classes.items():
                for obj in self.__session.query(val).all():
                    key = str(obj.__class__.__name__) + "." + str(obj.id)
                    objs[key] = obj
        return (objs)

    def new(self, obj):
        """Adds object obj to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes obj from the session if it is not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
            Creates all tables in the database,
            creates the current database session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """call remove() method on the private session attribute
        (self.__session) or close() on the class Session
        """
        self.__session.close()
