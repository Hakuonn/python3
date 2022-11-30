from tkinter import *
import time

root = Tk()
clock = Label(root,font=('Times',20,'bold'),bg='skyblue')
clock.pack(fill=Y,expand=1)

def tick():
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    clock.after(200,tick)

time1 = time.strftime('%H:%M:%S')
tick()
root.mainloop()