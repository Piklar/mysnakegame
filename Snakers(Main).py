import os
from tkinter import *

root = Tk()
root.title('Welcome to Snakers!')


def clickeasy():
    os.system('Place the local directory address of Snakers.easy here')
#Please look at line 9 print function and change it

def clickmedium():
    os.system('Place the local directory address of Snakers.medium here')
#Please look at line 13 print function and change it

def clickhard():
    os.system('Place the local directory address of Snakers.hard here')
#Please look at line 17 print function and change it

def exit():
    quit()


label = Label(root, text='Welcome to Snakers!!')
label2 = Label(root, text='Choose a Difficulty')
button1 = Button(root, text='Easy', command=clickeasy)
button2 = Button(root, text='Medium', command=clickmedium)
button3 = Button(root, text='Hard', command=clickhard)
button4 = Button(root, text='Exit Game', command=exit)

label.grid(row=0, column=2)
label2.grid(row=1, column=2)
button1.grid(row=4, column=1)
button2.grid(row=4, column=2)
button3.grid(row=4, column=3)
button4.grid(row=5, column=2)

root.mainloop()
