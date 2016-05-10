from flask import Flask,Blueprint
from pymongo import MongoClient
from bson.json_util import dumps
app = Flask(__name__)
client=MongoClient()

test_bp=Blueprint('test_flask',__name__)

@test_bp.route('/test')
def helloworld():
  db = client.employee
  return dumps(db.employees.find())
