import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb['customers']

print('-'*10,'原資料','-'*10)
for i in mycol.find():
    print(i)

qfield,qdata = input('選擇要刪除的欄位(name , country , address)&開頭字母:').split(' ')
print('-'*10,'刪除了幾筆資料？','-'*10)
myquery = {qfield:{'$regex':('^'+qdata)}}
x = mycol.delete_many(myquery)
print(x.deleted_count,'documents deleted.')

print('-'*10,'將%s開頭=%s刪除後的資料'%(qfield,qdata),'-'*10)
for i in mycol.find():
    print(i)

