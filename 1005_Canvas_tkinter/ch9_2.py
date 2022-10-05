from tkinter import *
import time
import math


def circle(canvas, x, y, r, color):
    canvas.create_oval(x-r, y-r, x+r, y+r, fill=color)


def line(canvas, x1, y1, x2, y2, color, size):
    canvas.create_line(x1, y1, x2, y2, fill=color, width=size)


def scale(canvas, x, y, j, size):
    for i in range(0, 360, j):
        r = 140
        x1 = x+r*math.cos(math.pi/180*i)
        y1 = y+r*math.sin(math.pi/180*i)
        r = 150
        x2 = x+r*math.cos(math.pi/180*i)
        y2 = y+r*math.sin(math.pi/180*i)
        line(w, x1, y1, x2, y2, 'black', size)


def text(canvas, x, y):
    for i in range(0, 360, 30):
        x1 = x+128*math.sin(math.pi/180*i)
        y1 = y-128*math.cos(math.pi/180*i)
        t = int(i/30)
        if t == 0:
            t = 12
        canvas.create_text(x1, y1, text=t, font=('bold', 16))


def pointer(canvas, x, y, r, point, color, size):
    x1 = x+r*math.sin(math.pi/180*point)
    y1 = y-r*math.cos(math.pi/180*point)
    canvas.create_line(x, y, x1, y1, fill=color, width=size)


def clock(w):
    circle(w, x, y, 140, 'white')
    time1 = time.strftime('%H:%M:%S')
    s = int(time1[6]+time1[7])*6
    m = int(time1[3]+time1[4])*6
    h = (int(time1[0]+time1[1]) % 12)*30+m/12
    text(w, x, y)
    pointer(w, x, y, 70, h, 'brown', 5)
    pointer(w, x, y, 110, m, 'blue', 4)
    pointer(w, x, y, 130, s, 'red', 2)
    circle(w, x, y, 5, 'black')
    root.after(1000, clock, w)


root = Tk()
width1 = 600
height1 = 400
w = Canvas(root, width=width1, height=height1, bg='green')
w.pack()

x = width1/2
y = height1/2
circle(w, x, y, 160, 'brown')
circle(w, x, y, 150, 'white')
scale(w, x, y, 6, 2)
scale(w, x, y, 30, 5)
text(w, x, y)
clock(w)
root.mainloop()
