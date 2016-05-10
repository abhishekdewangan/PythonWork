
class GCM:
    def __init__(self,client):
        self.client = client
    def __init__(self):
        print "construtor with no argument is called"

    def sendPushNotify(self,dict,name):
         print "push notification called"
         print "gcm obj is ",self.client
         msg=name+"is inserted"
         for id in dict:
            result=self.client.send(id,msg)
            print "--push result is:",result.successes

    def getGcmClient(self):
        return self.client