import tkinter as tk


root = tk.Tk()
root.title('C110156217')
mycanvas = tk.Canvas(root, width=500, height=500)
mycanvas.pack()

#  橢圓
mycanvas.create_oval(60, 290, 230, 410)

# 直線
mycanvas.create_line(60, 260, 85, 300)

# text
mycanvas.create_text(145, 350, text="我全都要", font=('微軟正黑體', 30))

# 三角
mycanvas.create_polygon(25, 100, 110, 100, 65, 55, fill='red')

# 矩形
mycanvas.create_rectangle(5, 130, 110, 250, fill='blue')
mycanvas.create_rectangle(35, 100, 95, 170, fill='white')
mycanvas.create_rectangle(45, 100, 90, 150, fill='#DEB887')

mycanvas.create_rectangle(150, 140, 240, 250, fill='gray')
mycanvas.create_rectangle(160, 100, 210, 140, fill='#DEB887')
mycanvas.create_rectangle(160, 60, 210, 100, fill='black')

# 多邊形
mycanvas.create_polygon(360, 360, 380, 310, 400, 360,
                        400, 400, 360, 400, fill='black')

root.mainloop()
