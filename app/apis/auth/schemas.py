LoginSchema = {
    'type': 'object',
    'properties': {
        'username': {'type': 'string', 'minLength': 5},
        'password': {'type': 'string', 'minLength': 8}
    },
    'required': ['username', 'password']
}
