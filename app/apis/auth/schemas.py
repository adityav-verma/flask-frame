LoginSchema = {
    'type': 'object',
    'properties': {
        'username': {'type': 'string', 'minlength': 5},
        'password': {'type': 'string', 'minlength': 8}
    },
    'required': ['username', 'password']
}
