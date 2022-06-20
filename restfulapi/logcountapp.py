from lib2to3.pgen2.parse import Parser
from flask import Flask
from flask_restful import Api, Resource

from logcount import get_time_data,get_hour_data,get_ip_data,get_os_data
app = Flask(__name__)
api = Api(app)


class IpAddress(Resource):
    # def abrot_if_data_doesnt_exit(id):
    #     if id not in get_ip_data():
    #         abort(404, message="User {} doesn't exist.".format(id))
    def get(self):
        return get_ip_data()
class Os(Resource):
    def get(self):
        return get_os_data()
class TimeData(Resource):
    def get(self):
        return get_time_data()
class HourData(Resource):
    def get(self):
        return get_hour_data()


api.add_resource(IpAddress, "/ipaddress")
api.add_resource(Os, "/os")
api.add_resource(TimeData, "/time")
api.add_resource(HourData, "/hour")

if __name__ == "__main__":
    app.run(debug=True)



