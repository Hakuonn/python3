from tkinter import *
import time
from tkinter.ttk import Progressbar

root = Tk()
root.title('Process Bar')
w = Canvas(root,bg='pink',width=600,height=400)
w.pack()

def run():
    progressBar['maximum'] = 100
    progressBar['value'] = 0
    color1 = [1,2,3,4,5]
    color1[0] = 'red'
    color1[1] = 'yellow'
    color1[2] = 'green'
    color1[3] = 'blue'
    color1[4] = 'violet'
    Label(root , text='   ',bg='green').place(x=320-140,y=350-30)
    r=100
    for i in range(0,101,5):
        progressBar['value']=i
        w.create_oval(320-(r-i),200-(r-i),320+(r-i),200+(r-i) , fill=color1[int(i/5)%5])
        time.sleep(0.2)
        Label(root , text=str(i) , bg='green').place(x=320-140,y=350-30)
        progressBar.update()

button1 = Button(root , bg='lime' , text='Run ProgressBar' , command=run)
button1.place(x=260,y=30)

progressBar = Progressbar(root,orient='horizontal',length=300,mode='determinate')
progressBar.place(x=320-140,y=350)

root.mainloop()