from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util

from sqlalchemy import create_engine, Column, String, Integer, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class TokenBase(Base):
    __tablename__ = 'token'

    user_id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)


class Token(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, user_id=None, expire_date=None):  # noqa: E501
        """Token - a model defined in OpenAPI

        :param id: The id of this Token.  # noqa: E501
        :type id: str
        :param user_id: The user_id of this Token.  # noqa: E501
        :type user_id: str
        :param expire_date: The expire_date of this Token.  # noqa: E501
        :type expire_date: datetime
        """
        self.openapi_types = {
            'id': str,
            'user_id': str,
            'expire_date': datetime
        }

        self.attribute_map = {
            'id': 'id',
            'user_id': 'user_id',
            'expire_date': 'expire_date'
        }

        self._id = id
        self._user_id = user_id
        self._expire_date = expire_date

    @classmethod
    def from_dict(cls, dikt) -> 'Token':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Token of this Token.  # noqa: E501
        :rtype: Token
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Token.


        :return: The id of this Token.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Token.


        :param id: The id of this Token.
        :type id: str
        """

        self._id = id

    @property
    def user_id(self) -> str:
        """Gets the user_id of this Token.


        :return: The user_id of this Token.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        """Sets the user_id of this Token.


        :param user_id: The user_id of this Token.
        :type user_id: str
        """

        self._user_id = user_id

    @property
    def expire_date(self) -> datetime:
        """Gets the expire_date of this Token.


        :return: The expire_date of this Token.
        :rtype: datetime
        """
        return self._expire_date

    @expire_date.setter
    def expire_date(self, expire_date: datetime):
        """Sets the expire_date of this Token.


        :param expire_date: The expire_date of this Token.
        :type expire_date: datetime
        """

        self._expire_date = expire_date
