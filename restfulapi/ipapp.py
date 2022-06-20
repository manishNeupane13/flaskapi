
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
# from flask_limiter import Limiter
# from flask_limiter.util import get_remote_address
from readaccesslog import access_log_data
from logcount import ip_data
app = Flask(__name__)
api = Api(app)

# Limiter = Limiter(app, key_func=get_remote_address)
# Limiter.init_app(app)

reqparser = reqparse.RequestParser()


# (reqparser.parse_args())


def abort_if_data_doesnt_exit(IP):
    if IP not in ip_data().keys():
        abort(404, message="IP {} doesn't exist".format(IP))


class IpAddress(Resource):
    def __init__(self):
        reqparser.add_argument('IP', type=str, required=True,
                               help="Please enter IP address")
        self.__ipaddress = reqparser.parse_args().get('IP',None)
        # self.__id=reqparser.parse_args().get('ID',None)
        
        

    def get(self):

       

        if self.__ipaddress in ip_data().keys():
            return {
            "response": 200,
            "ipaddress": self.__ipaddress,
            "Total Number ": ip_data()[self.__ipaddress]
        }
        else:
            return{"response": 400}


api.add_resource(IpAddress, "/ipaddress/")


class IpDetails(Resource):
    def __init__(self):
        # self.__ipaddress = reqparser.parse_args().get('IP', None)
        reqparser.add_argument('ID', type=int, required=True,
                               help="Please enter IP address")
        self.__id=reqparser.parse_args().get('ID',None)

    def get(self):

            return {
                "response": "Sucessful",
                "Data":access_log_data()[self.__id]
                        
                # "ipaddress": self.__ipaddress,
                # "Total Number ": ip_data()[self.__ipaddress]
            }


api.add_resource(IpDetails, "/details/")


if __name__ == "__main__":
    app.run(debug=True)
