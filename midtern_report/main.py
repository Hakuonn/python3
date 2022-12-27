from tkinter import *
import threading
import time
import random

map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
       [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
       [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
       [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
       [1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
       [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
       [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
       [1, 0, 1, 1, 1, 1, 0, 0, 1, 2, 1, 0, 0, 1, 2, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


def rightKey(event):
    global pacd
    pacd = 0
    print('right')


def downKey(event):
    global pacd
    pacd = 1
    print('down')


def leftKey(event):
    global pacd
    pacd = 2
    print('left')


def upKey(event):
    global pacd
    pacd = 3
    print('up')


def drawmap(w, img):
    for my in range(0, 12):
        for mx in range(0, 32):
            w.create_image(mx*30, my*30, anchor=NW, image=img[map[my][mx]])


def Ghost(w, xy, di1, color):
    ex = 0
    ey = 0
    iv = [2, 3, 0, 1]
    dl = [0, 0, 0, 0]
    w.create_image(xy[0]*30, xy[1]*30, anchor=NW, image=img[map[xy[1]][xy[0]]])
    od1 = iv[di1[0]]
    if map[xy[1]][xy[0]+1] % 2 == 0:
        dl[0] = 1
    if map[xy[1]+1][xy[0]] % 2 == 0:
        dl[1] = 1
    if map[xy[1]][xy[0]-1] % 2 == 0:
        dl[2] = 1
    if map[xy[1]-1][xy[0]] % 2 == 0:
        dl[3] = 1
    while True:
        count = dl[0]+dl[1]+dl[2]+dl[3]
        if count == 1:
            di1[0] = od1
            break
        ch = random.randint(0, 3)
        if (dl[ch] == 1 and ch != od1):
            di1[0] = ch
            break
    if di1[0] == 0:
        xy[0] = xy[0]+1
    if di1[0] == 1:
        xy[1] = xy[1]+1
    if di1[0] == 2:
        xy[0] = xy[0]-1
    if di1[0] == 3:
        xy[1] = xy[1]-1
    # draw ghost
    x = xy[0]*30
    y = xy[1]*30
    # body
    w.create_arc(x+3, y, x+30-3, y+60, start=0,
                 extent=180, fill=color, width=1)
    w.create_oval(x+6, y+9, x+14, y+17, fill="white", width=1)
    w.create_oval(x+16, y+9, x+24, y+17, fill="white", width=1)
    # eye
    if di1[0] == 0:
        ex = 1
        ey = 0
    if di1[0] == 1:
        ex = 0
        ey = 1
    if di1[0] == 2:
        ex = -1
        ey = 0
    if di1[0] == 3:
        ex = 0
        ey = -1
    w.create_oval(x+9+ex, y+12+ey, x+11+ex, y+14+ey, fill="black", width=2)
    w.create_oval(x+19+ex, y+12+ey, x+21+ex, y+14+ey, fill="black", width=2)
    # leg
    w.create_arc(x+13, y+26, x+17, y+34, start=0,
                 extent=180, fill="black", width=1)
    w.create_arc(x+6, y+26, x+10, y+34, start=0,
                 extent=180, fill="black", width=1)
    w.create_arc(x+20, y+26, x+24, y+34, start=0,
                 extent=180, fill="black", width=1)


def pacman(w, xy, di, color):
    global sw
    global pacd
    w.create_image(xy[0]*30, xy[1]*30, anchor=NW, image=img[map[xy[1]][xy[0]]])
    if pacd == 0 and map[xy[1]][xy[0]+1] % 2 == 0:
        xy[0] = xy[0]+1
        di[0] = 0
    if pacd == 1 and map[xy[1]+1][xy[0]] % 2 == 0:
        xy[1] = xy[1]+1
        di[0] = 1
    if pacd == 2 and map[xy[1]][xy[0]-1] % 2 == 0:
        xy[0] = xy[0]-1
        di[0] = 2
    if pacd == 3 and map[xy[1]-1][xy[0]] % 2 == 0:
        xy[1] = xy[1]-1
        di[0] = 3

    if (map[xy[1]][xy[0]] == 0):
        map[xy[1]][xy[0]] = 2
    x = xy[0]*30
    y = xy[1]*30
    if di[0] == 0:
        if sw == 0:
            w.create_arc(x, y, x+30, y+30, start=30, extent=300,
                         fill="yellow", width=3)  # 右開嘴
        else:
            w.create_arc(x, y, x+30, y+30, start=0, extent=359,
                         fill="yellow", width=3)  # 右合嘴
    if di[0] == 1:
        if sw == 0:
            w.create_arc(x, y, x+30, y+30, start=-60, extent=300,
                         fill="yellow", width=3)  # 下開嘴
        else:
            w.create_arc(x, y, x+30, y+30, start=-90, extent=359,
                         fill="yellow", width=3)  # 下合嘴
    if di[0] == 2:
        if sw == 0:
            w.create_arc(x, y, x+30, y+30, start=150, extent=-
                         300, fill="yellow", width=3)  # 左開嘴
        else:
            w.create_arc(x, y, x+30, y+30, start=180, extent=-
                         359, fill="yellow", width=3)  # 左合嘴
    if di[0] == 3:
        if sw == 0:
            w.create_arc(x, y, x+30, y+30, start=60, extent=-
                         300, fill="yellow", width=3)  # 上開嘴
        else:
            w.create_arc(x, y, x+30, y+30, start=90, extent=-
                         359, fill="yellow", width=3)  # 上合嘴
    sw = ~sw


def draw(w):
    # --Pacman
    xy = [1, 1]
    di = [0]
    # --Ghost red
    xy1 = [1, 10]
    di1 = [0]
    # --Ghost blue
    xy2 = [15, 10]
    di2 = [0]
    # new
    # --Ghost purple
    xy3 = [30, 10]
    di3 = [0]

    drawmap(w, img)
    while True:
        pacman(w, xy, di, "yellow")  # xy存x,y座標list , di存pacman方向list
        if xy[0] == xy1[0] and xy[1] == xy1[1]:
            w.create_text(480, 180, fill="yellow",
                          font="Arial 35 bold", text="Game Over!")
            break
        Ghost(w, xy1, di1, "red")
        if xy[0] == xy1[0] and xy[1] == xy1[1]:
            w.create_text(480, 180, fill="red",
                          font="Arial 35 bold", text="Game Over!")
            break
        Ghost(w, xy2, di2, "blue")
        if xy[0] == xy2[0] and xy[1] == xy2[1]:
            w.create_text(480, 180, fill="blue",
                          font="Arial 35 bold", text="Game Over!")
            break
        # new
        Ghost(w, xy3, di3, "violet")
        if xy[0] == xy3[0] and xy[1] == xy3[1]:
            w.create_text(480, 180, fill="violet",
                          font="Arial 35 bold", text="Game Over!")
            break

        time.sleep(0.2)


# main
sw = 0
pacd = 4

root = Tk()
root.title("PacMan")

w = Canvas(root, width=960, height=360, bg="black")
w.pack()

root.bind('<Left>', leftKey)
root.bind('<Right>', rightKey)
root.bind('<Down>', downKey)
root.bind('<Up>', upKey)
root.bind('<a>', leftKey)
root.bind('<d>', rightKey)
root.bind('<s>', downKey)
root.bind('<w>', upKey)
root.bind('<A>', leftKey)
root.bind('<D>', rightKey)
root.bind('<S>', downKey)
root.bind('<W>', upKey)

img = []
for i in range(4):
    img.insert(i, PhotoImage(file="map" + str(i) + ".png"))

t = threading.Thread(target=draw, args=(w,)).start()

root.mainloop()
