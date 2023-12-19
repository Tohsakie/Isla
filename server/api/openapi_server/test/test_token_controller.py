import unittest

from flask import json

from openapi_server.models.token import Token  # noqa: E501
from openapi_server.test import BaseTestCase


class TestTokenController(BaseTestCase):
    """TokenController integration test stubs"""

    def test_get_token(self):
        """Test case for get_token

        Request a token
        """
        query_string = [('user_id', 'user_id_example')]
        headers = { 
            'Accept': 'application/json',
            'api_key': 'special-key',
        }
        response = self.client.open(
            '/token',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
