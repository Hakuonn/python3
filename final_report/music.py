import requests
import json
#憑證
def get_access_token():
    url = 'https://account.kkbox.com/oauth2/token' #api網址
    # 標頭
    headers = {
        "Host":"account.kkbox.com",
        "Content-Type":"application/x-www-form-urlencoded"
    }
    # 參數
    data = {
        "grant_type": "client_credentials",
        "client_id": "7a374022c0170e6e7fdf4a9372ea404a",
        "client_secret": "4461cc97a1f4db563a64be9dac4a35db"
    }
    
    access_token = requests.post(url , headers=headers , data=data)
    return access_token.json()["access_token"]

# get_access_token()

#排行榜查詢
def get_charts():
    #取得憑證
    access_token = get_access_token()
    #取得排行榜api網址
    url = "https://api.kkbox.com/v1.1/charts"
    #標頭
    headers = {
        "accept" :"application/json",
        "authorization": "Bearer " + access_token
    }
    #參數
    parmas = {
        "territory" : "TW"
    }
    respone = requests.get(url , headers=headers , params=parmas)
    result = respone.json()['data']

    data = []
    for item in result:
        print(item['id'],item['title'])
        data.append({
            'id' : item['id'],
            'title' : item['title'],
            'url' : item['url']
        })
    with open('data/charts.json' , 'w' , encoding='utf8') as f:
        f.write(json.dumps(data , indent=4 , ensure_ascii=False))
# get_charts()

#取得該音樂排行榜的歌曲列表
def get_charts_tracks(chart_id):
    access_token = get_access_token()
    url = "https://api.kkbox.com/v1.1/charts/" + chart_id + "/tracks"
    #標頭
    headers = {
        'accept': "application/json",
        'authorization': "Bearer " + access_token
    }
    #參數
    parmas = {
        "territory" : "TW"
    }
    response = requests.get(url , headers=headers , params=parmas)
    result = response.json()['data']
    data = []
    for item in result:
        # print(item['name'],item['url'])
        data.append({
            'name' : item['name'],
            'url' : item['url']
        })
    return data

#儲存至各個排行榜json檔
def store_charts_tracks():
    with open('data/charts.json' , 'r') as f:
        charts = json.load(f)
    for item in charts:
        data = get_charts_tracks(item['id'])
        if item['title'] == '獨立/另類單曲週榜':
            item['title'] = '獨立_另類單曲週榜'
        elif item['title'] == '有聲書 / 相聲單曲週榜':
            item['title'] = '有聲書_相聲單曲週榜'
        with open('data/%s.json'%(item['title']) , 'w' , encoding='utf8') as f:
            f.write(json.dumps(data,indent=4,ensure_ascii=False))


store_charts_tracks()