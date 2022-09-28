import tkinter as tk
print(tk.TkVersion)
root = tk.Tk()
root.title("C110156217")
mycanvas = tk.Canvas(root, width=500, height=500)
mycanvas.pack()

mycanvas.create_text(400, 400, text='Hello World')

mycanvas.create_line(50, 10, 400, 50, fill='blue')

mycanvas.create_rectangle(210, 10, 300, 200, fill='Yellow')

mycanvas.create_arc(110, 10, 200, 100)

mycanvas.create_oval(10, 10, 100, 100, fill='green')

mycanvas.create_polygon(40, 40, 60, 20, 80, 40, 80, 80, 40, 80, fill='black')

root.mainloop()
