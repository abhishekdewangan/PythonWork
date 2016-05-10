from flask import Flask,request,jsonify
from pymongo import MongoClient
from bson.json_util import dumps
from DatabaseOperation import dbOperations
from flask_pushjack import FlaskGCM

app = Flask(__name__)
config = {
    'GCM_API_KEY': 'AIzaSyDZ5OFi-kNx-DVKwvPKsVrwS3VHaWYvjXc'
}
app.config.update(config)
client = FlaskGCM()
client.init_app(app)

dbGcmUsers=MongoClient()
@app.before_request
def beforeRequest():
    print "beforeRequest() called"
    print client

@app.route('/register',methods=["POST"])
def register():
     print request.headers
     if request.headers['Content-Type'] == 'application/json':
        try:
            print "content type is json"
            db = dbGcmUsers.gcmuser
            try:
                userDetails =request.get_json()
            except:
                return jsonify({'status':0,'result':"request is not in json format"})

            print "request json",userDetails
            dbOperations.insert(userDetails)
            sendPushNotification(dbOperations.getAllRegIds())
            return  jsonify({'status':1,'result':"Reg Id Successfully added in server"})

        except:
            return jsonify({'status':0,'result':"error in registering RegId"})

     else:
        return jsonify({'status':0,'result':"cotent type is application/json"})

def sendPushNotification(token):
    res = client.send(token,"wake up  sid")
    # List of requests.Response objects from GCM Server.
    print "Responses+++++",res.responses

    # List of messages sent.
    print "Messages++++++",res.messages

    # List of registration ids sent.
    print "Registration Ids +++++",res.registration_ids

    # List of server response data from GCM.
    print "push data +++",res.data

    # List of successful registration ids.
    print "successful reg id's",res.successes

    # List of failed registration ids.
    print "failed reg id's",res.failures


    # List of exceptions.
    print "push exceptions",res.errors

    # List of canonical ids (registration ids that have changed).
    print "canonical ids",res.canonical_ids


if __name__ == '__main__':
    app.run(host='172.27.46.216')
