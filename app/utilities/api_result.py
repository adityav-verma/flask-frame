from flask import Response
import json


class ApiResult(object):
    """Api result to be used across the application"""
    def __init__(self, payload, message=None, status=200):
        if type(payload) != dict:
            return ValueError('Type of payload should be dict')
        self.payload = payload
        self.message = message
        self.status = status

    def to_response(self):
        """Return a JSON response"""
        response = {
            'message': self.message,
            'payload': self.payload
        }
        return Response(
            json.dumps(response), self.status, mimetype='application/json'
        )
