from tkinter import Tk, Label
import time

master = Tk()
master.title("Digital Clock")

def get_time():
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200, get_time)

#title = Label(master, font=("Arial", 20, "bold"), text="Digital Clock", fg="pink", bg="black", pady=10)
#title.pack()

clock = Label(master, font=("Stencil", 90, "bold"), bg="black", fg="pink", bd=30, relief="sunken")
clock.pack()

get_time()

master.mainloop()
