from textwrap import fill
import threading
import time
import tkinter as tk
from tracemalloc import start

root = tk.Tk()
root.title('小精靈')

h = 600
w = 600
c = tk.Canvas(root , width=w , height=h , bg='black')
c.pack()

def job():
    r = 100
    while True():
        c.create_arc(400+r,400+r,400-r,400-r,start=30,extent=300,fill='white')
        time.sleep(0.1)
        c.create_arc(400+r,400+r,400-r,400-r,start=30,extent=300,fill='red')
        time.sleep(0.1)
        c.create_arc(400+r,400+r,400-r,400-r,start=30,extent=300,fill='orange')
        time.sleep(0.1)
        c.create_arc(400+r,400+r,400-r,400-r,start=30,extent=300,fill='yellow')
        time.sleep(0.1)
        c.create_arc(400+r,400+r,400-r,400-r,start=30,extent=300,fill='green')
        time.sleep(0.1)
        c.create_arc(400+r,400+r,400-r,400-r,start=30,extent=300,fill='blue')
        time.sleep(0.1)
        c.create_arc(400+r,400+r,400-r,400-r,start=30,extent=300,fill='violent')
        time.sleep(0.1)
        c.create_arc(400+r,400+r,400-r,400-r,start=30,extent=300,fill='purple')
        time.sleep(0.1)

t= threading.Thread(target=job)
t.start()
root.mainloop()