from flask import Flask
from pymongo import MongoClient
from bson.json_util import dumps
app = Flask(__name__)
client=MongoClient()

@app.route('/')
def helloworld():
  db = client.employee
  return dumps(db.employees.find())

if __name__ == '__main__':
    app.run(host='172.27.46.216')