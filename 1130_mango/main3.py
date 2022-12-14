import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['mydatabase']
mycol = mydb['customers']
 #  如果沒有自己設_id 則mongodb會自己創建
mylist=[
    {'_id':1,'name':'Uber','country':'Taiwan','address':'Hill Avenue, Nazareth,pa, 18064','age':31},
    {'_id':2,'name':'BMW','country':'USA','address':'Elgin Road, Richmond,va, 23223','age':24},
    {'_id':3,'name':'HONDA','country':'Janap','address':'Mehani Place, Kapolei,hi, 96707','age':19},
    {'_id':4,'name':'Toyota','country':'Taiwan','address':'Roundhouse Road, Spooner,wi, 54801','age':45},
    {'_id':5,'name':'Vicaky','country':'UK','address':'S Trindle Street, Hugoton,ks, 67951','age':21},
    {'_id':6,'name':'Viola','country':'HongKong','address':'Navaho Drive, Rocky Mount,mo, 65072','age':18},
    {'_id':7,'name': 'Uber','country': 'Taiwan','address': 'Roundhouse Beautiful Road, Spooner,wi','age': 29},
    {'_id':8,'name':'Rolex','country':'HongKong','address':'Elgin Road, Richmond, Rocky Mount','age':69}
]
x = mycol.insert_many(mylist)
print(x.inserted_ids)
