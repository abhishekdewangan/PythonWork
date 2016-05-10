from flask import Flask,request,jsonify,Response
from pymongo import MongoClient
from bson.json_util import dumps
import requests
import json
import os

app = Flask(__name__)
client=MongoClient()

ROOTPath = os.path.dirname(os.path.abspath(__file__))
target = os.path.join('C:\Users\abhishekdewa\PycharmProjects\untitled','/images')
if not os.path.isdir(target):
  os.mkdir(target)


@app.route("/")
def data():
    print "Root path is:-->",ROOTPath
    print "target path is :---->",target
    return "hello How are you???"

@app.route('/data',methods=["POST"])
def helloworld():
  #data =request.stream.read()
  data = request.json
  print data
  params = request.get_json()['name']
  print ("ALL PARAMETER",params)
  return "Abhishek"
  '''resultdata =request.stream.read;
  return resultdata
  if request.headers['content-type'] == 'application/json':


      request.json =json.loads(data)

      print "content type success"
      json_data = request.get_json(force=True, silent=True)
      if not json_data:
        return jsonify(error="Bad JSON request")
      result = []

      username =request.get_json['name']
      print username
      password =request.get_json['password']
      print  password
      if username == "admin" and password == "password":
            db = client.employee
            return dumps(db.employees.find())
  else:
     return {'errorMsg':"loginerror"}'''

@app.route("/student/<name>")
def student(name):
    return '<h2>'+name+'<h2>'

if __name__ == '__main__':
    app.run(debug=True)
