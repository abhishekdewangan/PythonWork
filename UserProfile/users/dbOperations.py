from pymongo import MongoClient

client =MongoClient()
db=client.gcmuser
def insert(json):
      print "insert call"
      name = json['name']
      print name
      emailid=json['emailId']
      print emailid
      regId=json['regId']
      print regId
      db.users.insert({
          'name':name,
          'emailId':emailid,
          'regId':regId
      })


def deleteByEmailId(emailid):
    db.users.remove({'emailId':emailid})

def getRegId(emailId):
    result =db.users.find({'emailId':emailId})
    return result

def getAllRegIds():
    regIds = []
    allResult = db.users.find();
    for data in allResult:
        regIds.append(data['regId'])
    print regIds
    return regIds
