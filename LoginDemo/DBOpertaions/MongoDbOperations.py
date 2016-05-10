from pymongo import MongoClient
from flask import jsonify,url_for,redirect
from DBOpertaions import ImageOperation
from bson.json_util import dumps

import json

mongo_client = MongoClient()
db = mongo_client.User

gcmClient = None

def insertIntoDB(json):
    name=json['name']
    regId =json['regId']
    email=json['emailId']
    password=json['password']
    count = db.Users.find({'emailId':{'$exists':'true','$eq':email}}).count()
    print "no of email id present ",count
    try:
        if(count==0):
            print "inside if"
            db.Users.insert({'name':name,'emailId':email,'password':password,'regId':regId})
            sendNotification(email,name)
            return jsonify({'status':1,"result":"RegisterSuccessful"})
        else:
            return jsonify({'status':0,"result":"Email Id is Already present in Database please login with email id "})
    except:
        return jsonify({'status':0,"result":"error in inserting into database please try again "})

def verifyUserLogin(loginDetails):
    email=loginDetails['emailId']
    password=loginDetails['password']
    loginResult =db.Users.find({'emailId':email,'password':password}).count()
    if(loginResult>0):
        return jsonify({'status':1,'result':"LOGIN SUCCESSFUL!!!!"})
    else:
        return jsonify({'status':0,'result':"LOGIN UNSUCCESSFUL!!!! Please Register EmailId"})

def createNewPassword(passwordDetails):
    email=passwordDetails['emailId']
    forgotCount = db.Users.find({'emailId':email}).count()
    if(forgotCount>0):
        newPass = passwordDetails['password']
        db.Users.update({'emailId':email},{'$set':{'password':newPass}})
        return jsonify({'status':1,'result':"Password Updated successfully"})
    else:
        return jsonify({'status':0,'result':"EmailId is not present in database please register email Id then try to Login"})

def removeAccount(removeDetail):
    removeEmail=removeDetail['emailId']
    removeCount=db.Users.find({'emailId':removeEmail}).count()
    if(removeCount>0):
        db.Users.remove({'emailId':removeEmail})
        return jsonify({'status':1,'result':"Account Removed Successfully"})
    else:
        return jsonify({'status':0,'result':"Account Does not exists !!!!!"})

def userDetails(userName):
    detailCount=db.Users.find({'name':userName}).count()
    print "detail count is :",detailCount
    if(detailCount>0):
       result =db.Users.find({'name':userName})
       json_string=dumps(result)
       new_json= json.loads(json_string)
       print "new json is :",new_json
       dict = {'status':1,'result':new_json}
       return dumps(dict)
    else:
        return jsonify({'status':0,'result':"email Id not found please provide valid email id"})

def updateUser(updatedDetail):
    email=updatedDetail['emailId']
    name=updatedDetail['name']
    img=updatedDetail['image']
    updateCount=db.Users.find({'emailId':email}).count()
    print "update count is:",updateCount
    if(updateCount>0):
       if(len(img)>0):
        print "image count is greater then 0 "
       # result =
        ImageOperation.upload_file(img,name)
        status = 1
        print "status is :--->",status
        if(status==1):
            url = ""+url_for('uploaded_file', filename=name+".png")
            try:
              db.Users.update({'emailId':email},{'$set':{'name':name,'image':url}})
              print "update successful when img>0"
              return jsonify({'status':1,'result':"Profile Updated successfully !!!!!"})
            except:
              print ("image count is > 0 but problem during uploading image")
              return jsonify({'status':0,'result':" Updation  Fail !!!!!"})


       else:
        print "image count is equal to 0 "
        try:
            redirect(url_for('uploaded_file', filename='default.png'))
            print "default image url:-->",url_for('uploaded_file', filename='default.png')
            try:
              db.Users.update({'emailId':email},{'$set':{'name':name,'image':url_for('uploaded_file', filename='default.png')}})
              print "db update success"
            except:
               print "problem in updating"
            return jsonify({'status':1,'result':"Profile Updated successfully !!!!!"})
        except:
            print "problem is updating file"
            return jsonify({'status':1,'result':"Profile Updatation fail !!!!!"})

    else:
        return jsonify({'status':0,'result':"User in not registered first register user"})


def sendNotification(id,name):
    notIdsList = db.Users.find({'emailId':{'$ne':id}}).count()
    if(notIdsList>0):
        IdList=db.Users.distinct('regId',{'emailId':{'$ne':id}})
        ids =dumps(IdList)
        AllIds=json.loads(ids)
        sendPushNotify(AllIds,name)

def sendPushNotify(dict,name):
         print "push notification called"
         print "gcm obj is ",gcmClient
         msg=name+"is inserted"
         for id in dict:
            result=gcmClient.send(id,msg)
            print "Responses+++++",result.responses

            # List of messages sent.
            print "Messages++++++",result.messages

            # List of registration ids sent.
            print "Registration Ids +++++",result.registration_ids

            # List of server response data from GCM.
            print "push data +++",result.data

            # List of successful registration ids.
            print "successful reg id's",result.successes

            # List of failed registration ids.
            print "failed reg id's",result.failures


            # List of exceptions.
            print "push exceptions",result.errors


def registerGCM(app):
    global gcmClient
    gcmClient = app
    print "gcm obj is created in MOngoDBOper",gcmClient


