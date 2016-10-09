from flask import jsonify


class APIError(Exception):

    def __init__(self, message, status=500):
        self.message = message
        self.status = status

    def to_response(self):
        response = jsonify({
            "message": self.message
        })
        response.status_code = self.status

        return response


class JWTError(APIError):

    def __init__(self, message, status=401):
        super().__init__(message, status)


class BadRequest(APIError):

    def __init__(self, message, status=400):
        super().__init__(message, status)
