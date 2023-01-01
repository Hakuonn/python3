from flask import Flask , render_template , url_for , redirect , request
from sqlalchemy_charts import select_charts
import sqlalchemy_tracks
import sqlalchemy_mylove
app = Flask(__name__)

#主頁面，選擇要查詢的排行榜
@app.route('/')
def index():
    data = select_charts()
    print(data)
    return render_template('home.html' , data=data)

#處理要查詢的排行榜資料,並轉址到tanking
@app.route('/submit' , methods=["POST"])
def submit():
    if request.method == "POST":
        rank_id = request.form['rank_id']
        ranktitle = request.form['ranktitle']
        if ranktitle == '有聲書 / 相聲單曲週榜':
            ranktitle = '有聲書 - 相聲單曲週榜'
        elif ranktitle == '獨立/另類單曲週榜':
            ranktitle = '獨立-另類單曲週榜'
        print(rank_id)
        print(ranktitle)
        return redirect(url_for('tanking',ranktitle=ranktitle))

#排行榜歌曲查詢
@app.route('/tanking/<ranktitle>')
def tanking(ranktitle):
    ranktitle = ranktitle
    if ranktitle == '有聲書 - 相聲單曲週榜':
        ranktitle = '有聲書 / 相聲單曲週榜'
    elif ranktitle == '獨立-另類單曲週榜':
        ranktitle = '獨立/另類單曲週榜'
    charts = sqlalchemy_tracks.select_charts(ranktitle)
    return render_template('ranking.html', **locals())

#更新
@app.route('/update' , methods=["POST"])
def update():
    if request.method == "POST":
        ranktitle = request.form['ranktitle']
        songname = request.form['songname']
        songlink = request.form['songlink']
        data = [ranktitle,songname,songlink]
        return render_template('ranking_name_update.html',data=data)

#更新完成後回到排行榜歌單
@app.route('/updating' , methods=["POST"])
def updating():
    if request.method == 'POST':
        newname = request.form['newname']
        ranktitle = request.form['ranktitle']
        songlink = request.form['songlink']
        sqlalchemy_tracks.update(ranktitle,newname,songlink)
        return redirect(url_for('tanking',ranktitle=ranktitle))
    
#刪除
@app.route('/delete',methods=["POST"])
def deleting():
    if request.method == 'POST':
        ranktitle = request.form['ranktitle'] 
        songname = request.form['songname']
        sqlalchemy_tracks.delete(ranktitle,songname)
        return redirect(url_for('tanking',ranktitle=ranktitle))



#============================================================
#我的最愛
@app.route('/mylove',methods=["POST"])
def mylvove():
    if request.method == 'POST':
        ranktitle = request.form['ranktitle']
        print(ranktitle)
        return redirect(url_for('tanking',ranktitle=ranktitle))
#列出歌單(查詢)
@app.route('/mylovepage',methods=["POST"])
def mylovepage():
    ranktitle = request.form['ranktitle']
    songname = request.form['songname']
    songlink = request.form['songlink']
    artist = request.form['artist']
    sqlalchemy_mylove.mylovesong(songname,songlink,artist)
    return redirect(url_for('tanking',ranktitle=ranktitle))

if __name__ == '__main__':
    app.run(debug=True)