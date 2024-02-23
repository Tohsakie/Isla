import connexion
from flask import Response
import pandas as pd

from typing import Dict
from typing import Tuple
from typing import Union

import json

from openapi_server.models.user import User  # noqa: E501
from openapi_server import util
import openapi_server.databases.postgres_connection as db


def create_user(user=None):  # noqa: E501
    """Create user

    Create a user # noqa: E501

    :param user: Created user object
    :type user: dict | bytes

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        user = User.from_dict(connexion.request.get_json())  # noqa: E501
        db.insert_user(user.to_dict())
        return Response(None, status=200)
    else:
        return Response("JSON only !", status=406)


def get_user_by_name(username):  # noqa: E501
    """Get user by user name

     # noqa: E501

    :param username: The name that needs to be fetched.
    :type username: str

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    return db.query("SELECT * FROM users WHERE username LIKE '%" + username + "%'").to_dict(orient="records")


def operate(input):  # noqa: E501
    """Send request to the system

    This request will first send a signal to the API Dispatcher, then a response from the system will be received. # noqa: E501

    :param input: The text input
    :type input: str

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """
    return 'do some magic!'