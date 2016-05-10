import os
import io
from Tkinter import Image
from flask import send_from_directory
from flask import Flask, request, redirect, url_for,jsonify
from werkzeug.utils import secure_filename
import base64

ROOTPath = os.path.dirname(os.path.abspath(__file__))
target = os.path.join(ROOTPath,'../gcm/profileImage')
if not os.path.isdir(target):
  os.mkdir(target)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = target

@app.route('/upload', methods=['POST'])
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
    except:
        print "error in creating url"

    return jsonify({'result':"successfully uploaded image"})


@app.route('/uploads/<filename>')
def uploaded_file(filename):
     return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == '__main__':
    app.run(host='172.27.46.216')