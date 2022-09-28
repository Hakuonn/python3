import threading
import time
import tkinter as tk
root = tk.Tk()
root.title('C110156217')
h = 600
w = 600
c = tk.Canvas(root, height=h, width=w, bg='blue')
c.pack()


def job():
    r = 60

    while True:
        c.create_arc(250+r, 250+r, 250-r, 250-r, start=30,
                     extent=300, width=10, fill='red')
        time.sleep(0.1)
        c.create_arc(250+r, 250+r, 250-r, 250-r, start=30,
                     extent=300, width=10, fill='yellow')
        time.sleep(0.1)
        c.create_arc(250+r, 250+r, 250-r, 250-r, start=30,
                     extent=300, width=10, fill='green')
        time.sleep(0.1)


t = threading.Thread(target=job)
t.start()
root.mainloop()
