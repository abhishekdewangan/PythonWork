import httplib, urllib
def main():
 params = urllib.urlencode({'username': 'admin', 'password': 'password'})
 conn = httplib.HTTPConnection("http://127.0.0.1",5000)
 conn.request("POST","http://127.0.0.1:5000/postdata",params,)
 response = conn.getresponse()
 print response.status, response.reason
 data = response.read()
 print data
 conn.close()

if __name__ == "__main__":
 # if you call this script from the command line (the shell) it will
 # run the 'main' function
 main()