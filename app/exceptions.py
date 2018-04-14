from app.utilities import ApiResult

class AppException(object):
    def __init__(self, payload, message, status=400):
        self.payload = payload
        self.message = message
        self.status = status

    def to_result(self):
        return ApiResult(
            payload=self.payload,
            message=self.message,
            status=self.status
        )
