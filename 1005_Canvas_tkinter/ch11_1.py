from tkinter import *

root = Tk()
w = Canvas(root,width=650,height=600,bg='blue')
w.pack()
# 上半短矩形
x = 650/2
y = 600/2
w1 = 35
w2 = 20
w.create_rectangle(x-w1+100,y-w2-20,x+w1+100,y+w2-20,fill='red',width=3,outline='black')
# 下半短矩形
w1 = 35
w2 = 20
w.create_rectangle(x-w1+100,y-w2+20,x+w1+100,y+w2+20,fill='yellow',width=3,outline='black')
# 上半長矩形
x = 650/2
y = 0
w1 = 25
w2 = 600/2-40-20
w.create_rectangle(x-w1+100,y-w2+20,x+w1+100,y+w2+20,fill='green',width=3,outline='black')
# 下半長矩形
x = 650/2
y = 600/2+140
w1 = 25
w2 = 120
w.create_rectangle(x-w1+100,y-w2+20,x+w1+100,y+w2+40,fill='white',width=3,outline='black')

root.mainloop()