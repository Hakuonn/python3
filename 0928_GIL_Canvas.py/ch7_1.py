import tkinter as tk
from PIL import Image, ImageTk
# img
root = tk.Tk()
root.title('C110156217')
img = Image.open('ok.png')
img2 = ImageTk.PhotoImage(img)
mycanvas = tk.Canvas(root, width=img.size[0], height=img.size[1])
mycanvas.pack()
mycanvas.create_image(0, 0, anchor=tk.NW, image=img2)
root.mainloop()