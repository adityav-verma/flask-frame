from flask import current_app
import requests

from app.utilities.services import BaseService


class UserAuthService(BaseService):
    def __init__(self):
        self.CLIENT_ID = current_app.config.get('OAUTH_CLIENT_ID')
        self.CLIENT_SECRET = current_app.config.get('OAUTH_CLIENT_SECRET')

    def login_user(self, username, password):
        """Log a user using oauth/login
        Args:
            - username (str)
            - password (str)
        Returns:
            - dict
            {
                'status_code': 2XX/4XX/5XX,
                'payload': {
                    'access_token': 'token',
                    'expires_in': 3600,
                    'token_type': 'Bearer',
                    'scope': 'email',
                    'refresh_token': 'token'
                }
            }
        """
        payload = {
            'username': username,
            'password': password,
            'client_id': self.CLIENT_ID,
            'client_secret': self.CLIENT_SECRET,
            'grant_type': 'password'
        }
        response = self.make_request(
            'POST', 'http://web:80/api/auth/oauth/token', payload
        )
        data = {
            'status_code': 400,
            'payload': response.json()
        }
        if response.status_code == requests.codes.ok:
            data['status_code'] = 200
        return data
