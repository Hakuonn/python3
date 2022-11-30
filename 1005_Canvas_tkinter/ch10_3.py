from tkinter import *
import threading
import time

global count # 建立全域變數

def job(w): # 先進行所需的餘數計算
    global count # 在函數內還需定義一次全域變數
    while True:
        segment(w,125,20,segnum[count%10]) # 以餘數做個位數
        segment(w,25,20,segnum[int(count/10)%10]) # ÷10後，以餘數做十位數
        time.sleep(1)
        count+=1

def segment(w,x,y,value):
    color = ['gray','red']
    w.create_oval(x,y,x+52,y+10,fill=color[int(value[0])]) #a
    w.create_oval(x+50,y+5,x+60,y+60,fill=color[int(value[1])]) #b
    w.create_oval(x+50,y+70,x+60,y+125,fill=color[int(value[2])]) #c
    w.create_oval(x,y+120,x+52,y+130,fill=color[int(value[3])]) #d
    w.create_oval(x-10,y+70,x,y+125,fill=color[int(value[4])]) #e
    w.create_oval(x-10,y+5,x,y+60,fill=color[int(value[5])]) #f
    w.create_oval(x,y+60,x+52,y+70,fill=color[int(value[6])]) #g

root = Tk()

# 七段顯示器組成字串
segnum = ['1111110','0110000','1101101','1111001','0110011','1011011','1011111','1110000','1111111','1111011']


w = Canvas(root,width=300,height=200,bg='black')
w.pack()

count=0

segment(w,125,20,segnum[0])
segment(w,25,20,segnum[0])

t = threading.Thread(target=job,args=(w,))
t.start()
root.mainloop()