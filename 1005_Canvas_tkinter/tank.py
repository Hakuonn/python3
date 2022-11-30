from tkinter import *
import math
import time
import random
import threading

def key(event):
    global theta,flag,t,v,tx,STOP
    if event.char == 'c' or event.char=='C':
        t=0
        flag=0
        theta=45*3.14159/180
        v=40
        STOP=1
        label.configure(text=v)
        w.coords(ball,0,0,0,0)
        #戰車
        tx = random.randint(480,700-60)
        w.coords(item1,0+tx,420,45+tx,430)
        w.coords(item2,27+tx,412,53+tx,485)
        w.coords(item3,10+tx,428,70+tx,452)
        #砲塔
        theta = 45*3.14159/180
        r=60
        x=r*math.cos(theta)
        y=r*math.sin(theta)
        r1=40
        w.coords(item,0,450,x,450-y)
    if event.char=='a' or event.char=='A':
        v+=1
    if event.char=='z' or event.char=='Z':
        v-=1
    label.configure(text=v)

    #發射子彈
def spacekey(event):
    global flag,theta,t
    t=0
    flag=-1

#控制砲管發射角度
def callback(event):
    global theta
    theta=math.atan(abs(event.y-450)/(event.x))
    x = r*math.cos(theta)
    y = r*math.sin(theta)
    event.widget.coords(item,0,450,x,450-y)
    return

def job(w):
    global theta,flag,t,r2,v,tx,wall,STOP
    r=6
    t=0
    while True:
        if flag==-1:
            if STOP==1:
                if t==0:
                    vx=v*math.cos(theta) #初始速度
                    vy=v*math.sin(theta)
                    lx=65*math.cos(theta) #砲管高度
                    ly=65*math.sin(theta)
                    x=vx*t
                    y=vy*t-t*t
                    w.coords(ball,lx+x-r,(450-y-ly)-r,lx+x+r,(450-y-ly)+r)
                #砲彈
                x=vx*t
                y=vy*t-t*t
                w.coords(ball,lx+x-r,(450-y-ly)-r,lx+x+r,(450-y-ly)+r)
                time.sleep(0.05)
                t=t+0.5
                print((450-y-ly)," ",450-r2)
                
                #判斷牆座標或已到地面
                if y<-1 or ((lx+x-r)>310 and (lx+x-r)<390 and (450-y-ly)>(450-r2)):
                    flag=0
                    w.delete(wall)
                    r2=random.randint(50,200)
                    # 牆壁
                    wall=w.create_rectangle(350-r1,450-r2,350+r1,450+r2,fill='gray',width=2)

                #判斷砲彈是否擊中坦克
                if ((lx+x-r)>tx and (lx+x-r)<tx+70) and y<0:
                    label.configure(text="Game Over")
                    STOP=0
        
root = Tk()
w = Canvas(root,width=700,height=450,bg='green')
w.pack()

root.bind("<space>",spacekey)
root.bind("<Button-1>",callback)
root.bind("<Key>",key)

flag=0
t=0
v=40
STOP=1

#砲台
theta=45*3.14159/180
r=60
x=r*math.cos(theta)
y=r*math.sin(theta)
r1=40
item=w.create_line(0,450,x,450-y,width=15)
w.create_oval(0-r1,450-r1,0+r1,450+r1,fill='gray',width=5)

#繪製牆壁
r1=40
r2=random.randint(50,200)
wall = w.create_rectangle(350-r1,450-r2,350+r1,450+r2,fill='gray',width=2)

#繪製戰車
tx=random.randint(480,700-60)
item1=w.create_rectangle(0+tx,420,45+tx,430,fill='brown',width=2)
item2=w.create_rectangle(27+tx,412,53+tx,485,fill='gray',width=2)
item3=w.create_rectangle(10+tx,428,70+tx,452,fill='black',width=2)

#速度
label = Label(w,text=v,bg='green',font=(None,24))
label.pack()
label.place(x=350,y=15)

#繪製球
ball=w.create_oval(0,0,0,0,fill='yellow',width=1)

t = threading.Thread(target=job,args=(w,))
t.start()

mainloop()