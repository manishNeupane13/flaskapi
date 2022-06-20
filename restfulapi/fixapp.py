from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse

app = Flask(__name__)
api = Api(app)


class HelloResource(Resource):
    def get(self):
        return {'message': 'Hello'}


class SayHiResource(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True,
                            help='Name cannot be blank',location='form')
        args = parser.parse_args()

        return {'message': 'Hello ' + args['name']}


api.add_resource(HelloResource, '/hello')
api.add_resource(SayHiResource, '/say-hi')

if __name__ == '__main__':
    app.run(debug=True, load_dotenv=True)
