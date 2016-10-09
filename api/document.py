from flask import request
import glob
from os.path import basename, splitext, getsize
import re

from . import api
from .helpers import Links, Resource
from .index import index_links

links = Links(id="id")


def get_text_list():
    texts = []
    files = glob.glob("./data/*.txt")
    for index in range(len(files)):
        texts.append(dict(
            id=index,
            name=splitext(basename(files[index]))[0],
            size=getsize(files[index])
        ))
    return texts


def get_texts():
    texts = []
    for f in glob.glob("./data/*.txt"):
        texts.append(get_text(f))
    return texts


def get_text(path):
    with open(path) as f:
        return f.read()

TEXT_LIST = get_text_list()
TEXTS = get_texts()


@api.route("/api/document/<id>")
@links.add("details")
class Document(Resource):

    def get(self, id):
        return TEXT_LIST[int(id)]


@api.route("/api/document/<id>/text")
@links.add("text")
class Text(Resource):

    def get(self, id):
        query = request.args.getlist("search")
        if query:
            query = query[0]
            if not query:
                raise BadRequest("Empty search parameter")
            pattern = re.compile(query)
            return [(m.start(0), m.end(0)) for m in re.finditer(pattern, TEXTS[int(id)])]
        return TEXTS[int(id)]


@api.route("/api/documents")
@index_links.add("documents")
class Documents(Resource):

    @links
    def get(self):
        return TEXT_LIST
