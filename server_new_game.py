# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 17:36:04 2019

@author: melkhafef
"""
import tkinter
import keyboard 
import _thread
from socket import *
s=socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
host="127.0.0.1"
port=9000
s.bind((host,port))
s.listen(5)
root = tkinter.Tk()
root.geometry('400x400')
root.title('server')
X=True
buttons=[]
fireballs1=[]
fireballs2=[]
b1=0
b2=0
for i in range(0,2):
    buttons.append(tkinter.Button(root,width=20))
buttons[0].pack()
buttons[1].pack()
x1=200
x2=200
y1=20
y2=360
count1=0
count2=0
buttons[0].place(x=x1,y=y1,width=50,height=20)
buttons[1].place(x=x2,y=y2,width=50,height=20)
buttons[0].config(bg='#d12044')
buttons[1].config(bg='#4420d1')
value1=tkinter.StringVar()
score1=tkinter.Label(textvariable=value1,fg='#d12044')
score1.pack()
score1.place(x=20,y=200)
value1.set(count1)
value2=tkinter.StringVar()
score2=tkinter.Label(textvariable=value2,fg='#4420d1')
score2.pack()
score2.place(x=340,y=200)
value2.set(count2)
c,a=s.accept()
def pressQ():
    global x1
    while True :
        keyboard.wait('q')
        x1-=10
        c.send('q'.encode('utf-8'))
        if x1>0 :
            buttons[0].place(x=x1,y=y1)
        else :
            x1=0
            buttons[0].place(x=x1,y=y1)
def pressW():
    global x1
    while True :
        keyboard.wait('w')
        x1=x1+10
        c.send('w'.encode('utf-8'))
        if x1<351 :
            buttons[0].place(x=x1,y=y1)
        else :
            x1=350
            buttons[0].place(x=x1,y=y1)
def pressZ():
    global x2
    x2-=10
    print(x2)
    if x2>0 :
        buttons[1].place(x=x2,y=y2)
    else :
        x2=0
        buttons[1].place(x=x2,y=y2)
def pressX():
    global x2
    x2=x2+10
    print(x2)
    if x2<351 :
        buttons[1].place(x=x2,y=y2)
    else :
        x2=350
        buttons[1].place(x=x2,y=y2)
def pressE():
    global x1,b1,count1
    while True :
        keyboard.wait('e')
        c.send('e'.encode('utf-8'))
        xball=x1+25
        yball=y1
        fireballs1.append(tkinter.Button(root,width=20))
        fireballs1[b1].pack()
        fireballs1[b1].place(x=xball,y=yball,width=10,height=10)
        fireballs1[b1].config(relief=tkinter.FLAT,bg='#d12e44')
        goal1=False
        for i in range(1300) :
            yball+=.3
            fireballs1[b1].place(x=xball,y=yball)
            if xball>=x2 and xball<=x2+50 and yball>=y2 and yball<=y2+10 and goal1==False :
                print("goal")
                count1+=1
                value1.set(count1)
                goal1=True    
        b1+=1
def pressC():
    global x2,b2,count2
    xball=x2+25
    yball=y2
    fireballs2.append(tkinter.Button(root,width=20))
    fireballs2[b2].pack()
    fireballs2[b2].place(x=xball,y=yball,width=10,height=10)
    fireballs2[b2].config(relief=tkinter.FLAT,bg='#442ed1')
    goal2=False
    for i in range(1300) :
        yball-=.3
        fireballs2[b2].place(x=xball,y=yball)
        if xball>=x1 and xball<=x1+50 and yball>=y1 and yball<=y1+10 and goal2==False :
            print("goal2")
            count2+=1
            value2.set(count2)
            goal2=True    
    b2+=1                  
_thread.start_new_thread(pressQ,())
_thread.start_new_thread(pressW,())
_thread.start_new_thread(pressE,())
def rec():
    while True:
        w=c.recv(2048)
        keypressed=w.decode('utf-8')
        if(keypressed=='x'):
            pressX()
        elif (keypressed=='z') :
            pressZ()
        elif (keypressed=='c'):
            pressC()
        print(keypressed)
_thread.start_new_thread(rec,())
root.mainloop()

