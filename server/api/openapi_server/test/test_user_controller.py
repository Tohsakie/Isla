import unittest

from flask import json

from openapi_server.models.user import User  # noqa: E501
from openapi_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_create_user(self):
        """Test case for create_user

        Create user
        """
        user = {"firstName":"John","lastName":"James","password":"12345","user_id":"dc92bf38-cce2-4f32-8fe3-b52806f8c352","email":"john@email.com","username":"XxIsla30xX"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/user',
            method='POST',
            headers=headers,
            data=json.dumps(user),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_by_name(self):
        """Test case for get_user_by_name

        Get user by user name
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/user/{username}'.format(username='username_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_operate(self):
        """Test case for operate

        Send request to the system
        """
        query_string = [('input', 'input_example')]
        headers = { 
            'Accept': 'plain/text',
        }
        response = self.client.open(
            '/operate',
            method='POST',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
