from flask import Flask, request
from flask_restplus import Api, Resource

from app.parsers.instagram import InstagramParser
from app.parsers.google import GoogleParser

app = Flask(__name__)
api = Api(app, doc='/help')


@api.route('/query')
class RouteInit(Resource):
    def get(self):
        params = request.args.to_dict()
        if not params.get('keyword'):
            return {'error': 1, 'msg': 'No keyword'}

        parser = InstagramParser()
        images = parser.get_images_by_keyword(params.get('keyword'))

        return {
            "keyword": params.get('keyword'),
            "error": 0,
            "msg": "",
            "images": images
        }


@app.route('/query_show')
def test():
    params = request.args.to_dict()

    Parser = InstagramParser

    if params.get('source', '').lower() == 'google':
        Parser = GoogleParser

    if not params.get('keyword'):
        return '<h1>No keyword</h1>'

    parser = Parser()
    images = parser.get_images_by_keyword(params.get('keyword'))

    return """
    '<h1>Images: </h1>'
    %s
    """ % "\n<br/>".join(
        ["<img src=\"%s\">" % img for img in images])
