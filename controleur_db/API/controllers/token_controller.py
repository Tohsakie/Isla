import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from API.models.token import Token  # noqa: E501
from API import util
import API.databases.postgres_connection as db

from flask import Response


def get_token(user_id):  # noqa: E501
    """Request a token

    It let you know if you have remaining credits # noqa: E501

    :param user_id: User that own tokens
    :type user_id: str
    :type user_id: str

    :rtype: Union[Token, Tuple[Token, int], Tuple[Token, int, Dict[str, str]]
    """
    return db.query("SELECT credit FROM users WHERE user_id = '" + user_id + "'").to_dict(orient="records")


def add_token(user_id, nb_token):
    db.add_token(user_id, nb_token)

    return Response(None, status=200)