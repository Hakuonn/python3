from tkinter import *
import math
import time
import random
import threading

def key(event):
    global theta,flag,t,v,tx,STOP
    if event.char == 'c' or event.char=='C':
        t=0
        flag=0
        theta=45*3.14159/180
        v=40
        STOP=1
        label.configure(text=v)
        w.coords(ball,0,0,0,0)