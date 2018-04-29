from flask import request
from jsonschema import validate


def validate_request_schema(schema):
    """Validate an API request against a Json Schema
    Raises:
        - ValidationError if request json is not valid for the given schema
        - SchemaError if invalid schema
    """
    def view_function_decorator(view_function):
        def wrapper(*args, **kwargs):
            validate(request.json, schema)
            return view_function(*args, **kwargs)
        return wrapper
    return view_function_decorator
