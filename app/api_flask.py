from flask import Flask

from app.utilities import ApiResult


class ApiFlask(Flask):
    """Override the Flask class to handle custom JSON Api Responses"""
    def make_response(self, rv):
        """Override Flask().make_response()
        Check if the type is ApiResult, then return ApiResult().to_response().
        """
        if isinstance(rv, ApiResult):
            return rv.to_response()
        return Flask.make_response(self, rv)
