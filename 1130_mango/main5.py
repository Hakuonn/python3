import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['python-tutorial']
mycol = mydb['customers']

myquery = {'name':'Viola'}
mydoc = mycol.find(myquery)
for i in mydoc:
    print(i)


