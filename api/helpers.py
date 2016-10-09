from functools import wraps

from flask import request
from flask.ext import restful

from . import api
from .errors import BadRequest
from .jwt import jwt_required


class Resource(restful.Resource):

    method_decorators = [jwt_required]


def link(rel, resource, method="GET", **kwargs):
    href = api.url_for(resource, **kwargs)
    return {"rel": rel, "href": href, "method": method}


class Link(object):

    def __init__(self, name, resource, condition, method):
        self.name = name
        self.resource = resource
        self.condition = condition
        self.method = method

    def to_url(self, args):
        return api.url_for(self.resource, **args)

    def to_dict(self, args):
        return {"rel": self.name,
                "href": self.to_url(args),
                "method": self.method}

    def should_be_added(self, resource):
        return self.condition(resource)


class Links(object):

    def __init__(self, condition=lambda x: True, **args):
        self.links = []
        self.to_pass = args
        self.condition = condition

    def add(self, name, condition=None, method="GET"):
        if condition is None:
            condition = self.condition

        def wrapper(cls):
            self.links.append(Link(name, cls, condition, method))
            return cls

        return wrapper

    def process(self, thing):
        if type(thing) is not dict:
            return thing

        args = {}
        for name_in_f, name_in_i in self.to_pass.items():
            args[name_in_f] = thing.get(name_in_i)

        links = []
        for link in self.links:
            if link.should_be_added(thing):
                links.append(link.to_dict(args))

        thing["_links"] = links

        return thing

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            ret = func(*args, **kwargs)
            if type(ret) is list:
                return [self.process(x) for x in ret]
            return self.process(ret)
        return wrapper
