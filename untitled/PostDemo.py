from flask import Flask,request,jsonify
from pymongo import MongoClient
from bson.json_util import dumps
from flask_httpauth import HTTPBasicAuth
from flask_basicauth import BasicAuth
app = Flask(__name__)
client=MongoClient()
auth = HTTPBasicAuth(app)
@app.route('/postdata',methods=["POST"])
def hellopost():
    print request.headers
    if request.headers['Content-Type'] == 'application/json':
        try:
            print "content type is json"
            #data = request.data
            data = request.get_json()['name']
            print "requested data" ,data
            db = client.employee
            return dumps(db.employees.find())
        except:
            return jsonify({'error':"error in post"})

    else:
        return jsonify({'error':"not json formet"})


if __name__ == '__main__':
    app.run(host='172.27.46.216')
