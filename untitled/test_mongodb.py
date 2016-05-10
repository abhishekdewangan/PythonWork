from pymongo import MongoClient

client = MongoClient()
db = client.employee
cursor = db.employees.find()

for document in cursor:
    print(document)