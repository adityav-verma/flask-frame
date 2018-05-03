import requests


class BaseService:
    def make_request(self, method, url, payload):
        if method == 'POST':
            return requests.post(
                url=url, data=payload
            )
