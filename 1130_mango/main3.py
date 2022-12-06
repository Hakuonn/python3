import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['mydatabase']
mycol = mydb['customers']
 #  如果沒有自己設_id 則mongodb會自己創建
mylist=[
    {'_id':1,'name':'Uber','country':'Taiwan'},
    {'_id':2,'name':'BMW','country':'USA'},
    {'_id':3,'name':'HONDA','country':'Janap'},
    {'_id':4,'name':'Toyota','country':'Taiwan'},
    {'_id':5,'name':'Vicaky','country':'UK'},
    {'_id':6,'name':'Viola','country':'HongKong'},
]
x = mycol.insert_many(mylist)
print(x.inserted_ids)