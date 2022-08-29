from tkinter import *
import tkinter
from datetime import datetime
import pyglet
pyglet.font.add_file("digital-7.ttf")


cor1 = "#DB2B39"  
cor2 = "#29335C"  
cor3 = "#21c25c"
cor4 = "#F3A712"  
cor5 = "##6B9AC4" 
cor6 = "#3080f0"


background = cor1
color = cor4

janela = Tk()
janela.title("")
janela.geometry("440x180")  # application window size - L-A
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=cor1) 


def watch():

    time = datetime.now()
    hour = time.strftime("%H:%M:%S")
    day_week = time.strftime("%A")
    day = time.day
    month = time.strftime("%B")
    year = time.strftime("%Y")

    l1.config(text=hour)
    l1.after(200,watch)
    l2.config(text= day_week +"  " + str(day) + "/" + str(month) + "/" + str(year))

    # print(hour)
    # print(day_week)
    # print(dia)
    # print(month)
    # print(year)


l1 = Label(janela, text="", font=(
    "digital-7 100"), bg=background, fg=color)
l1.grid(row=0, column=0, sticky=NW, padx=5)


l2 = Label(janela, text="", font=(
    "digital-7 17"), bg=background, fg=color)
l2.grid(row=1, column=0, sticky=NW, padx=5)




watch()
janela.mainloop()  # run
