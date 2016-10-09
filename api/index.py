from . import api
from .helpers import Links, Resource
from .jwt import is_verified

index_links = Links(condition=lambda x: is_verified())


@api.route("/api/")
class Index(Resource):

    # Explicitly remove jwt_required decorator
    method_decorators = []

    @index_links
    def get(self):
        return {}
