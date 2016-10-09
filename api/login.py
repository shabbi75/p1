from flask.ext.restful.reqparse import RequestParser

from . import api
from .errors import BadRequest
from .helpers import Resource
from .index import index_links
from .jwt import generate_token, is_verified

parser = RequestParser(bundle_errors=True)
parser.add_argument("username", required=True)
parser.add_argument("password", required=True)


@api.route("/api/login")
@index_links.add("login", method="POST", condition=lambda x: not is_verified())
class Login(Resource):

    method_decorators = []

    def post(self):
        args = parser.parse_args()
        if args["username"] == "ssh" and args["password"] == "homework":
            return {"token": generate_token(args["username"])}

        raise BadRequest("Login failed")
