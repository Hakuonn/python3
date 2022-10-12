import tkinter as tk
from PIL import Image, ImageTk
# img
root = tk.Tk()
root.title('C110156217')
img = Image.open('meme.png')
img2 = ImageTk.PhotoImage(img)
mycanvas = tk.Canvas(root, width=img.size[0], height=img.size[1])
mycanvas.pack()
mycanvas.create_image(0, 0, anchor=tk.NW, image=img2) #anchor -> 設定影像輸出在該區域的位置
root.mainloop()
