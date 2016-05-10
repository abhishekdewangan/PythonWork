from flask import Flask,send_from_directory
from flask_pushjack import FlaskGCM
from Services import RegisterService
from DBOpertaions import MongoDbOperations

import os

app = Flask(__name__)

config = {
    'GCM_API_KEY': 'AIzaSyBC8HEFxRtUxBNYi0iayiQRt1hR8c46sis'
}

app.config.update(config)
client = FlaskGCM()
client.init_app(app)


ROOTPath = os.path.dirname(os.path.abspath(__file__))
target = os.path.join(ROOTPath,'profileImages')
if not os.path.isdir(target):
  os.mkdir(target)

app.config['UPLOAD_FOLDER'] = target

app.register_blueprint(RegisterService.register_bp)
MongoDbOperations.registerGCM(client)

def getGCmClient():
    return client


@app.route('/')
def main():
    print "target path",target
    print "root path",ROOTPath
    return "main route"

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    print 'uploaded file called'
    result= send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
    return result



if __name__ == '__main__':
    app.run(host='172.27.46.216')