
import json
from demodata import user_information
from flask import Flask,jsonify


app=Flask(__name__)
@app.route('/get',methods=['GET'])
def get_information():
    return jsonify(json.dumps(user_information))


@app.route('/get/<int:id>', methods=['GET'])
def get_id(id):
    for i in range(len(user_information)):
        if user_information[i]['id']==id:
            return jsonify(user_information[i])
    return jsonify("No information found")

@app.route('/newpost',methods=['POST'])
def new_method():
    new_data = {"id": 6,
                "E-mail": "Sharku Khan@gmail.com",
                "name": "Sharkuh Khan",
                "address": "Satdobato",
                "Contact Number ": "9985632147"}
    user_information.append(new_data)

    return jsonify({"created":user_information})

@app.route('/put/<int:id>',methods=["PUT"])
def put_method(id):
    user_information[id-1]['name']="xyz"
    return jsonify(user_information[id-1])

@app.route('/delete/<int:id>',methods=['DELETE'])
def delete_method(id):
    for i in range(len(user_information)):
        if user_information[i]['id']==id:
            user_information.remove(user_information[i])
            return jsonify({'resutl':'Delete sucessfull.'})
    return jsonify("No information found")
    
if __name__=="__main__":
    app.run(debug=True)
