from flask import Flask, request , jsonify
import json

# Data to be written
dictionary = {
    "id": "04",
    "name": "sunil",
    "department": "HR"
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
        data="hello world"
        return jsonify(dictionary)

@app.route('/home/<int:num>', methods = ['GET'])
def disp(num):
  
    return jsonify({'data': num**2})

if __name__=="__main__":
    app.run(debug=True)
