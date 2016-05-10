from pymongo import MongoClient
client =MongoClient()
db=client.gcmuser
def insert(json):
      regId=json['regId']
      print regId
      db.gcmuser.insert({
          'regId':regId
      })


def deleteByEmailId(emailid):
    db.users.remove({'emailId':emailid})

def getRegId(emailId):
    result =db.users.find({'emailId':emailId})
    return result

def getAllRegIds():
    regIds = []
    allResult = db.gcmuser.find();
    for data in allResult:
        regIds.append(data['regId'])
    print regIds
    return regIds
