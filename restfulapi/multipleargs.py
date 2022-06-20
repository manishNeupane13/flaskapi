
try:
    from flask import Flask
    from flask_restful import reqparse, Api, Resource

except Exception as e:
    print("Some Modules are missing {}".format(e))

app = Flask(__name__)
api = Api(app)


# parser=reqparse.RequestParser()
parser = reqparse.RequestParser()
parser.add_argument('zip', type=str, required=True,
                    help="Please enter Zip code")
parser.add_argument('city', type=str, required=True, help="Please enter city")


class MyApi(Resource):
    def __init__(self):
        self.__zip_code = parser.parse_args().get('zip', None)
        self.__city = parser.parse_args().get('city', None)

    def get(self):
        if len(self.__city) > 2 and len(self.__zip_code) > 2:
            return {"Response": 200,
                    "Data": parser.parse_args()}
        else:
            return {"response": 400}


api.add_resource(MyApi, '/address')


if __name__ == "__main__":
    app.run(debug=True)
