from concurrent.futures import thread
from tkinter import *
import threading
import time


# 石柱開啟
def drawopenbar(w):
    # 上半短矩形
    x = 325
    y = 260
    w1 = 35
    w2 = 20
    w.create_rectangle(x-w1+100, y-w2-20, x+w1+100, y+w2-20,
                    fill='yellow', width=3, outline='black')
    # 下半短矩形
    w1 = 35
    w2 = 20
    w.create_rectangle(x-w1+100, y-w2+20+80, x+w1+100, y+w2+20+80,
                    fill='yellow', width=3, outline='black')
    # 上半長矩形
    x = 325
    y = 0
    w1 = 25
    w2 = 600/2-120
    w.create_rectangle(x-w1+100, y-w2+20, x+w1+100, y+w2+40,
                    fill='yellow', width=3, outline='black')
    # 下半長矩形
    x = 325
    y = 480
    w1 = 25
    w2 = 120
    w.create_rectangle(x-w1+100, y-w2+20, x+w1+100, y+w2+100,
                    fill='yellow', width=3, outline='black')
    # 覆蓋青蛙飛過的路徑
    w.create_rectangle(325-139,300-39,325+139,300+39,fill='blue',width=0)


# 石柱關閉
def drawclosebar(w):
    x = 325
    y = 300
    w1 = 35
    w2 = 20
    # 覆蓋青蛙飛過的路徑
    w.create_rectangle(325-139,210,325+139,300+39,fill='blue',width=0)

    # 上半短矩形
    w.create_rectangle(x-w1+100, y-w2-20, x+w1+100, y+w2-20,
                    fill='yellow', width=3, outline='black')
    # 下半短矩形
    w.create_rectangle(x-w1+100, y-w2+20, x+w1+100, y+w2+20,
                    fill='yellow', width=3, outline='black')
    # 上半長矩形
    y = 0
    w1 = 25
    w2 = 240
    w.create_rectangle(x-w1+100, y-w2+20, x+w1+100, y+w2+20,
                    fill='yellow', width=3, outline='black')
    # 下半長矩形
    y = 440
    w2 = 120
    w.create_rectangle(x-w1+100, y-w2+20, x+w1+100, y+w2+40,
                    fill='yellow', width=3, outline='black')
    
# 每點擊滑鼠右鍵一次，flag相反
def rightClick(event):
    global flag
    flag=~flag

# 飛行蛙動作變換
def drawfrog(w,x1,y1,ox,oy):
    global sw
    global img
    global img1
    # 繪製一矩形覆蓋前一張青蛙圖片
    w.create_rectangle(ox,oy,ox+82,oy+60,fill='blue', width=0)
    if sw == 0:
        w.create_image(x1,y1,anchor=NW,image=img1)
    else:
        w.create_image(x1,y1,anchor=NW,image=img2)
    sw =~ sw

# 青蛙的飛行和石柱的控制
def draw(w):
    global flag
    global sw
    drawopenbar(w) # 遊戲一開始石柱開啟
    x = 0
    y = 100
    ox = x
    oy = y
    while True:
        if flag != 0:
            drawfrog(w,x,y,ox,oy)
            drawclosebar(w)
            if x>340 and x<450:
                w.create_image(x,y,anchor=NW,image=img3)
            flag =~ flag
            time.sleep(0.05)
        drawopenbar(w)
        drawfrog(w,x,y,ox,oy)
        time.sleep(0.05)
        ox=x
        oy=y
        x = x+10
        y = y+5
        if x>360:
            y=280
        if x>500:
            x=0
            y=100
# main
sw = 0
flag = 0
root = Tk()
w = Canvas(root,width=650,height=600,bg='blue')
w.pack()
w.bind('<Button-1>',rightClick)

img1 = PhotoImage(file='f1.png')
img2 = PhotoImage(file='f2.png')
img3 = PhotoImage(file='f3.png')

drawopenbar(w)

t = threading.Thread(target=draw,args=(w,))
t.start()
root.mainloop()