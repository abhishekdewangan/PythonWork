from flask import Flask,request,jsonify,Blueprint
from pymongo import MongoClient
from bson.json_util import dumps
from flask_pushjack import FlaskGCM
from users import dbOperations

gcm_bp = Blueprint('gcm',__name__)
'''
app = Flask(__name__)
config = {
    'GCM_API_KEY': 'AIzaSyD39ZdRc8tzIQJn2hK2n7V3juPnH86jmAY'
}
app.config.update(config)
client = FlaskGCM()
client.init_app(app)
'''
@gcm_bp.route('/register',methods=["POST"])
def register():
     print request.headers
     print "in post before content-Type"
     if request.headers['Content-Type'] == 'application/json':
        print "in post"
        try:
            print "content type is json"
            userDetails =request.get_json()
            print userDetails
            dbOperations.insert(userDetails)
            return "register successful"

        except:
            return jsonify({'error':"error in post"})

     else:
        return jsonify({'error':"not json formet"})

def sendPushNotification(token):
    res = client.send(token,"Hello prasoon Fuck you")
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


