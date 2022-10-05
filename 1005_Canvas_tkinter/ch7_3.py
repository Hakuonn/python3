from tkinter import *
import time
import threading

flag=-1
def b1():
    global flag
    flag =~ flag
    if flag == -1:
        button1['text'] = 'go'
    else:
        button1['text'] = 'stop'
    print(flag)


def drawlight(num):
    c.create_oval(w/2-r,h/2-r,w/2+r,h/2+r,fill='black')
    c.create_oval(w/2-r-100,h/2-r,w/2+r-100,h/2+r,fill='black')
    c.create_oval(w/2-r+100,h/2-r,w/2+r+100,h/2+r,fill='black')
    if num == 0 :
        c.create_oval(w/2-r,h/2-r,w/2+r,h/2+r,fill='black')
        c.create_oval(w/2-r-100,h/2-r,w/2+r-100,h/2+r,fill='black')
        c.create_oval(w/2-r+100,h/2-r,w/2+r+100,h/2+r,fill='black')
    if num == 1 :
        c.create_oval(w/2-r-100,h/2-r,w/2+r-100,h/2+r,fill='green')
    if num == 2 :
        c.create_oval(w/2-r,h/2-r,w/2+r,h/2+r,fill='yellow')
    if num == 3 :
        c.create_oval(w/2-r+100,h/2-r,w/2+r+100,h/2+r,fill='red')

root = Tk()
BF = Frame(root)
BF.pack()
h=400
w=400
r=35
c=Canvas(root,height=h,width=w,bg='blue')
c.pack()
button1 = Button(root,text='go',fg='black',bg='brown',command=b1)
button1.pack()
button1.place(x=h/2-15,y=4)

c.create_rectangle(w/2-150,h/2-60,w/2+150,h/2+60,fill='brown')
c.create_oval(w/2-r,h/2-r,w/2+r,h/2+r,fill='black')
c.create_oval(w/2-r-100,h/2-r,w/2+r-100,h/2+r,fill='black')
c.create_oval(w/2-r+100,h/2-r,w/2+r+100,h/2+r,fill='black')
def job():
    while True:
        if flag == 0:
            drawlight(1)
            time.sleep(0.5)
            drawlight(2)
            time.sleep(0.5)
            drawlight(3)
            time.sleep(1)
        if flag == -1:
            drawlight(0)
            time.sleep(0.5)
            


t = threading.Thread(target=job)
t.start()
root.mainloop()
