
from flask import Flask
from flask_restful import reqparse, Api, Resource

from flask_limiter.util import get_remote_address
from flask_limiter import Limiter

from flasgger import Swagger
from flasgger.utils import swag_from
from flask_restful_swagger import swagger



# except Exception as e:
#     print("Some Modules are missing {}".format(e))



app = Flask(__name__)
api = Api(app)

Limiter = Limiter(app, key_func=get_remote_address)
Limiter.init_app(app)

api=swagger.docs(Api(app),apiVersion='1',api_spec_url='/doc')

class MyApi(Resource):
    decorators=[Limiter.limit("5/day")]
    @swagger.model
    @swagger.operation(notes='some really good notes')
    def get(self,city,zip):
        return {"Response":200,"city":city,"Zip Code":zip}

        

api.add_resource(MyApi,'/address/<string:city>/<string:zip>')
if __name__=="__main__":
    app.run(debug=True) 