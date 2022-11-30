import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['python-tutorial']
mycol = mydb['customers']

for i in mycol.find():
    print(i)