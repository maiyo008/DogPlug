"""
Contains the class DBStorage
"""
import models
from models.base_model import BaseModel, Base
from models.county import County
from models.dog import Dog
from models.groomer import Groomer
from models.location import Location
from models.owner import Owner
from models.review import Review
from models.service import Service
from models.town import Town
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {
            "BaseModel": BaseModel,
            "County": County,
            "Dog": Dog,
            "Groomer": Groomer,
            "Location": Location,
            "Owner": Owner,
            "Review": Review,
            "Service": Service,
            "Town": Town
        }

class DBStorage():
    """ Interacts with MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        DOGPLUG_MYSQL_USER = getenv('DOGPLUG_MYSQL_USER')
        DOGPLUG_MYSQL_PWD = getenv('DOGPLUG_MYSQL_PWD')
        DOGPLUG_MYSQL_HOST = getenv('DOGPLUG_MYSQL_HOST')
        DOGPLUG_MYSQL_DB = getenv('DOGPLUG_MYSQL_DB')
        DOGPLUG_ENV = getenv('DOGPLUG_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(DOGPLUG_MYSQL_USER,
                                             DOGPLUG_MYSQL_PWD,
                                             DOGPLUG_MYSQL_HOST,
                                             DOGPLUG_MYSQL_DB),
                                             pool_pre_ping=True)
        if DOGPLUG_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the curret database session all objects of the given class.
        If cls is None, queries all types of objects.
        Return:
            Dict of queried classes in the format <class name>.<obj id> = obj.
        """
        if cls is None:
            objs = self.__session.query(County).all()
            objs.extend(self.__session.query(Dog).all())
            objs.extend(self.__session.query(Groomer).all())
            objs.extend(self.__session.query(Location).all())
            objs.extend(self.__session.query(Owner).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Service).all())
            objs.extend(self.__session.query(Town).all())
        else:
            if isinstance(cls, str):
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session