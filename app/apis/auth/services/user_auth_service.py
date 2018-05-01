from flask import current_app

from app.utilities.services import BaseService


class UserAuthService(BaseService):
    def __init__(self):
        self.CLIENT_ID = current_app.config.get('OAUTH_CLIENT_ID')
        self.CLIENT_SECRET = current_app.config.get('OAUTH_CLIENT_SECRET')

    def login_user(self, username, password):
        payload = {
            'username': username,
            'password': password,
            'client_id': self.CLIENT_ID,
            'client_secret': self.CLIENT_SECRET,
            'grant_type': 'password'
        }
        response = self.make_request(
            'POST', 'http://localhost:8001/api/auth/oauth/token', payload
        )
        
        return response.json()
