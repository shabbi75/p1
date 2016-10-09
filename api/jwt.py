from datetime import datetime, timedelta
from functools import wraps

import jwt
from flask import current_app, request, _request_ctx_stack
from werkzeug.local import LocalProxy

from .errors import JWTError

current_user = LocalProxy(lambda: getattr(_request_ctx_stack.top,
                                          "current_user", None))


def jwt_required(func):

    @wraps(func)
    def decorator(*args, **kwargs):
        verify()
        return func(*args, **kwargs)

    return decorator


def is_verified():
    try:
        verify()
    except JWTError:
        return False
    return True


def verify():
    header = request.headers.get("Authorization", None)
    if header is None:
        raise JWTError("Missing header Authorization")

    parts = header.split()

    if len(parts) != 2:
        raise JWTError("Malformed header Authorization")

    secret_key = current_app.config.get("SECRET_KEY")
    try:
        payload = jwt.decode(parts[1], secret_key, algorithms=['HS512'])
    except jwt.exceptions.InvalidTokenError as e:
        raise JWTError(str(e))

    if "username" not in payload:
        raise JWTError("Invalid Payload (No username)")

    setattr(_request_ctx_stack.top, "current_user",
            {"username": payload["username"]})


def generate_token(user):
    secret_key = current_app.config.get("SECRET_KEY")
    delta = current_app.config.get("JWT_DELTA", timedelta(minutes=30))
    now = datetime.utcnow()
    return str(jwt.encode(
        {"exp": now + delta,  # expiration
         "nbf": now,  # not before
         "iat": now,  # issued at
         "username": user if type(user) is str else user["username"]},
        secret_key, algorithm='HS512'), "utf-8")
