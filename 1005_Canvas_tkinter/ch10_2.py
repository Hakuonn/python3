from tkinter import *
import threading

root = Tk()

w = Canvas(root,width=300,height=200,bg='black')
w.pack()

def segment(w,x,y,value):
    color = ['gray','red']
    w.create_oval(x,y,x+52,y+10,fill=color[int(value)])
    w.create_oval(x+50,y+5,x+60,y+60,fill=color[int(value)])
    w.create_oval(x+50,y+70,x+60,y+125,fill=color[int(value)])
    w.create_oval(x,y+120,x+52,y+130,fill=color[int(value)])
    w.create_oval(x-10,y+70,x,y+125,fill=color[int(value)])
    w.create_oval(x-10,y+5,x,y+60,fill=color[int(value)])
    w.create_oval(x,y+60,x+52,y+70,fill=color[int(value)])

dx = 70
segment(w,15+dx,30,1)
segment(w,100+dx,30,1)
root.mainloop()