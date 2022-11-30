from tkinter import *
import random

def spacekey(event):
    print('space')
    w.delete(ALL)
    w.create_oval(random.randint(1,201),random.randint(1,201),random.randint(1,201),random.randint(1,201),fill='red')


root = Tk()

w = Canvas(root,width=300,height=300,bg='green')
w.pack()

root.bind("<space>",spacekey)
root.mainloop()  