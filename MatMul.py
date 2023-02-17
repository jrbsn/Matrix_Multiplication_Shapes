import numpy as np
import random
from tkinter import*
from tkinter import font as tkFont

list1 = [0, 1, 2]
list2 = [list1[2], 1, 2]
print(list2)

def calculate():
    m1 = np.random.rand(int(m1c1.get()), int(m1c2.get()))
    m2 = np.random.rand(int(m2c1.get()), int(m2c2.get()))
    m3 = np.dot(m1,m2)
    m3_shape = str(m3.shape)
    outputvar.set(m3_shape)

master = Tk()
master.geometry('500x300')

maincolor = 'AntiqueWhite2'
scndcolor = 'AntiqueWhite2'
rectcolor = "AntiqueWhite2"

master['bg'] = maincolor
canvas = Canvas(master, width=150, height=150, bg=rectcolor)
canvas.place(x=330,y=100)

outputvar = StringVar()

titlefont = ("Helvetica", 20, "bold")
mainfont = ("Helvetica", 15)

mat1_y = 110
mat2_y = 160

title = Label(master, text="Matrix Shape Calculator", font=titlefont, bg=maincolor).place(x=90,y=15)

m1c1 = Entry(master, width=5, font=mainfont)
m1c1.place(x=150,y=mat1_y)
mat1 = Label(master, text="Matrix 1:", font=mainfont, bg=maincolor).place(x=20,y=mat1_y)
comma1 = Label(master, text="x", font=mainfont, bg=maincolor).place(x=215,y=mat1_y)
m1c2 = Entry(master, width=5, font=mainfont)
m1c2.place(x=235,y=mat1_y)

m2c1 = Entry(master, width=5, font=mainfont)
m2c1.place(x=150,y=mat2_y)
mat2 = Label(master, text="Matrix 2:", font=mainfont, bg=maincolor).place(x=20,y=mat2_y)
comma2 = Label(master, text="x", font=mainfont, bg=maincolor).place(x=215,y=mat2_y)
m2c2 = Entry(master, width=5, font=mainfont)
m2c2.place(x=235,y=mat2_y)

canvas.create_rectangle(330, 100, 480, 250, outline="black")
Label(master,text="Matrix 3:", font=mainfont, bg=scndcolor).place(x=365,y=110)
Label(master,text="(M1 x M2)", font=mainfont, bg=scndcolor).place(x=355,y=140)
output_label = Label(master,font=titlefont, textvariable=outputvar, bg=scndcolor).place(x=370,y=200)

button = Button(master, text="Calculate Shape", font=mainfont, command=calculate).place(x=142,y=215)

master.mainloop()