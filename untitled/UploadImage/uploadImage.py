
import os
import io
from Tkinter import Image
from flask import send_from_directory
from flask import Flask, request, redirect, url_for,jsonify
from werkzeug.utils import secure_filename
import base64

#UPLOAD_FOLDER = '/path/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

ROOTPath = os.path.dirname(os.path.abspath(__file__))
target = os.path.join(ROOTPath,'../gcm/images')
if not os.path.isdir(target):
  os.mkdir(target)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = target

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def getdata():
    print "root path---->",ROOTPath
    print "target path--->",target

@app.route('/data', methods=['POST'])
def upload_file():

    print "before post"
    if request.method == 'POST':
        json = request.get_json()['img']
        name=request.get_json()['name']
        filename=name+".png"
        destination = "/".join([target,filename])
        data = base64.b64decode(json)
        try:
            file = open(destination,'wb+')
            print os.path.abspath(filename)
            file.write(data)
            file.close()

        except:
            print "error in file"
    try:

        redirect(url_for('uploaded_file',
                                    filename=filename))
        print "url is :",url_for('uploaded_file', filename=filename)
        return jsonify({"url":url_for('uploaded_file', filename=filename)})
        uploaded = uploaded_file(filename)
        print "uploaded file :",uploaded
        print "uploaded file succesful"
        print "url is :",url_for('uploaded_file',filename)
    except:
        print "error in creating url"

    return jsonify({'result':"successfully uploaded image"})


@app.route('/uploads/<filename>')
def uploaded_file(filename):
     return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == '__main__':
    app.run(host='172.27.46.216')
