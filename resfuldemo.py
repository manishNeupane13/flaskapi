
from flask import Flask,request,jsonify
from flask_restful import Resource, Api
myapp=Flask(__name__)
myapi=Api(myapp)


#making class for a particular resource
#get and post mthods correpond to get and pot requests
# automaticall mapped by flask_restful
class Hello(Resource):

    def get(self):
        return jsonify({'message':"hello word"})
    
    def post(self):
        data=request.get_json()
        return jsonify({'data':data})
class Square(Resource):

    
      
    def get(self, num):
        if num%2==0:
             status="even"
        else:
            status="odd"
  
        return jsonify({'square': num**2,'status':status})
class even_odd(Resource):
    def get(self,num):
        if num%2==0:
             status="even"
        else:
            status="odd"
        return jsonify({'value':num,'status':status})
myapi.add_resource(Hello,'/hello')
myapi.add_resource(even_odd,'/pair/<int:num>')
myapi.add_resource(Square, '/square/<int:num>')
if __name__=="__main__":
     myapp.run(debug=True)

