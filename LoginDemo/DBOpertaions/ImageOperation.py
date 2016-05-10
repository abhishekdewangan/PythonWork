import os
from flask import redirect, url_for,jsonify,Blueprint
import base64

ROOTPath = os.path.dirname(os.path.abspath(__file__))
target = os.path.join(ROOTPath,'../profileImages')
if not os.path.isdir(target):
  os.mkdir(target)

upload_bp=Blueprint('ImageOperation',__name__)

def upload_file(encoadedImage,name):
        print "inside upload file"
        filename=name+".png"
        destination = "/".join([target,filename])
        data = base64.b64decode(encoadedImage)
        print "decoded data :--->",data
        try:
            file = open(destination,'wb+')
            print os.path.abspath(filename)
            file.write(data)
            file.close()
            redirect(url_for('uploaded_file',
                                    filename=filename))
            print "url is :",url_for('uploaded_file', filename=filename)
            url=""+url_for('uploaded_file', filename=filename)
            print "url for user profile is :-->",url

        except:
            print "upload file except"



