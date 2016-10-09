import types

from flask import Flask
from flask.ext import restful

from .errors import APIError

api = restful.Api(catch_all_404s=True)


def api_route(self, *args, **kwargs):
    def wrapper(cls):
        self.add_resource(cls, *args, **kwargs)
        return cls
    return wrapper

api.route = types.MethodType(api_route, api)

from . import (index, login, document)  # noqa


def create_app(settings):

    app = Flask(__name__)
    app.config.update(**settings)

    api.init_app(app)

    @app.errorhandler(APIError)
    def handle_ups_error(error):
        return error.to_response()

    return app
