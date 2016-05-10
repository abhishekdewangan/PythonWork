from flask import Blueprint,request,jsonify
from DBOpertaions import MongoDbOperations

register_bp=Blueprint('RegisterService',__name__)
flaskobj=None

@register_bp.route('/register',methods=["POST"])
def register():
    print "register header :",request.headers
    print "register json:-->",request.get_json()
    print "content type is:--->",request.headers['Content-Type']
    if request.headers['Content-Type'] == 'application/json':
        responseJson = request.get_json()
        print "response Json",responseJson
        try:
            return MongoDbOperations.insertIntoDB(responseJson)
        except:
            return jsonify({'result:':"Registration Failed"})

    else:
        print "error:request is not json type"
        return jsonify({'error':"request is not json type"})

@register_bp.route('/login',methods=["POST"])
def login():
     if request.headers['Content-Type'] == 'application/json':
        loginResponse = request.get_json()
        try:
           loginResult= MongoDbOperations.verifyUserLogin(loginResponse)
           return loginResult
        except:
            return jsonify({'error':'please provide proper key in json'})

     else:
         return jsonify({'error':"request is not json type"})

@register_bp.route('/forgotPassword',methods=["POST"])
def forgot_password():
    if request.headers['Content-Type'] == 'application/json':
        forgotJson = request.get_json()
        try:
            result= MongoDbOperations.createNewPassword(forgotJson)
            return result
        except:
            return jsonify({'status':0,'result':"Error in Forgot Password  please try again"})
    else:
         return jsonify({'error':"request is not json type"})

@register_bp.route('/delete',methods=['POST'])
def deleteAccount():
     if request.headers['Content-Type'] == 'application/json':
        removeJson = request.get_json()
        try:
            return MongoDbOperations.removeAccount(removeJson)
        except:
            return jsonify({'status':0,"result":"problem in deleting Account please try again!!!"})
     else:
         return jsonify({'error':"request is not json type"})


@register_bp.route('/details/<username>',methods=['GET'])
def getUserDetails(username):
   print "getUserDetails called"
   return MongoDbOperations.userDetails(username)

@register_bp.route('/update',methods=['POST'])
def updateUser():
    print "update user"
    if request.headers['Content-Type'] == 'application/json':
        updateJson=request.get_json()
        print "updated json is :",updateJson
        updateResponse=MongoDbOperations.updateUser(updateJson)
        return  updateResponse


