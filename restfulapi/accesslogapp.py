from readaccesslog import access_log_data
from flask import Flask
from flask_restful import Api, Resource, abort
app = Flask(__name__)
api = Api(app)

log_data = access_log_data()


def abrot_if_data_doesnt_exit(id):

    if id not in access_log_data():
        abort(404, message="User {} doesn't exist.".format(id))


class User(Resource):
    def get(self, id):
        abrot_if_data_doesnt_exit(id)
        return log_data[id]

    def delete(self, id):
        print("delte")
        abrot_if_data_doesnt_exit(id)
        del log_data[id]['Hour']
        return 'Deletion sucessful', 201

    def put(self, id):
        abrot_if_data_doesnt_exit(id)
        log_data[id]['Hour']="07"
        return "Update sucessfull",201



class AddUser(Resource):
    def get(self):
        return log_data


api.add_resource(User, "/getlog/<int:id>")
api.add_resource(AddUser, "/getlog")

if __name__ == "__main__":
    app.run(debug=True)
