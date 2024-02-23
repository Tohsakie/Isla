from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from API.models.base_model import Model
from API import util

from sqlalchemy import create_engine, Column, String, Integer, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import uuid

Base = declarative_base()

class UserBase(Base):
    __tablename__ = 'users'

    user_id = Column(String, primary_key=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)
    credit = Column(Integer)


class User(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, user_id=None, username=None, first_name=None, last_name=None, email=None, password=None, credit=None):  # noqa: E501
        """User - a model defined in OpenAPI

        :param user_id: The user_id of this User.  # noqa: E501
        :type user_id: str
        :param username: The username of this User.  # noqa: E501
        :type username: str
        :param first_name: The first_name of this User.  # noqa: E501
        :type first_name: str
        :param last_name: The last_name of this User.  # noqa: E501
        :type last_name: str
        :param email: The email of this User.  # noqa: E501
        :type email: str
        :param password: The password of this User.  # noqa: E501
        :type password: str
        :param credit: The credit of this User.  # noqa: E501
        :type password: int
        """
        self.openapi_types = {
            'user_id': str,
            'username': str,
            'first_name': str,
            'last_name': str,
            'email': str,
            'password': str,
            'credit': int
        }

        self.attribute_map = {
            'user_id': 'user_id',
            'username': 'username',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'email': 'email',
            'password': 'password',
            'credit': 'credit'
        }

        self._user_id = user_id
        self._username = username
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._password = password
        self._credit = credit

    @classmethod
    def from_dict(cls, dikt) -> 'User':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The User of this User.  # noqa: E501
        :rtype: User
        """
        return util.deserialize_model(dikt, cls)

    @property
    def user_id(self) -> str:
        """Gets the user_id of this User.


        :return: The user_id of this User.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        """Sets the user_id of this User.


        :param user_id: The user_id of this User.
        :type user_id: str
        """

        self._user_id = user_id

    @property
    def username(self) -> str:
        """Gets the username of this User.


        :return: The username of this User.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this User.


        :param username: The username of this User.
        :type username: str
        """

        self._username = username

    @property
    def first_name(self) -> str:
        """Gets the first_name of this User.


        :return: The first_name of this User.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        """Sets the first_name of this User.


        :param first_name: The first_name of this User.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def last_name(self) -> str:
        """Gets the last_name of this User.


        :return: The last_name of this User.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """Sets the last_name of this User.


        :param last_name: The last_name of this User.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def email(self) -> str:
        """Gets the email of this User.


        :return: The email of this User.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this User.


        :param email: The email of this User.
        :type email: str
        """

        self._email = email

    @property
    def password(self) -> str:
        """Gets the password of this User.


        :return: The password of this User.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this User.


        :param password: The password of this User.
        :type password: str
        """

        self._password = password

    @property
    def credit(self) -> str:
        """Gets the credit of this User.


        :return: The credit of this User.
        :rtype: str
        """
        return self._credit

    @credit.setter
    def credit(self, credit: str):
        """Sets the credit of this User.


        :param credit: The credit of this User.
        :type credit: str
        """

        self._credit = credit