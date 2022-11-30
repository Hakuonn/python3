import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['python-tutorial']
mycol = mydb['customers']

qmethod = input('選擇查詢方式（_id or name or country）：')
if qmethod == '_id':
    query = int(input('輸入 %s：' %(qmethod)))
else:
    query = input('輸入 %s：' %(qmethod))
myquery = {qmethod:query}
mydoc = mycol.find(myquery)
for i in mydoc:
    print(i)