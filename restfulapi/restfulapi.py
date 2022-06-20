
from demodata import user_information
from flask import Flask
from flask_restful import reqparse,abort,Api,Resource


app=Flask(__name__)
api=Api(app)

def abrot_if_data_doesnt_exit(id):
        if id not in user_information:
            abort(404,message="User {} doesn't exist.".format(id))
    
class User(Resource):
    def get(self,id):
        abrot_if_data_doesnt_exit(id)
        return user_information[id]
    def delete(self,id):
        abrot_if_data_doesnt_exit(id)
        del user_information[id]
        return 'Deletion sucessful',204
    def put(self,id):
        abrot_if_data_doesnt_exit(id)
        user_information[id]['E-mail']="neupanemanes1475@gmail.com"
        return user_information,201

class AddUser(Resource):
    def get(self):
        return user_information
    def post(self):
        new_data ={"E-mail": "Sharku Khan@gmail.com",
                    "name": "Sharkuh Khan",
                    "address": "Satdobato",
                    "Contact Number ": "9985632147"}
        key_value = len(user_information)+1
        user_information[key_value]=new_data
        return user_information[key_value],201
    # user_information.append(new_data)

    #     return user_information


api.add_resource(User,"/userinfo/<int:id>")
api.add_resource(AddUser,"/addinfo")

if __name__=="__main__":
    app.run(debug=True)
