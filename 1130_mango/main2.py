import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['mydatabase']
print(myclient.list_database_names()) #列印database name list
mycol = mydb['customers']
collist = mydb.list_collection_names()
if 'customers' in collist:
    print('the database exists')