#!usr/bin/python

import inspect												#print (inspect.getargspec(tkinter.Text))
from tkinter import *
import os
import sys
import subprocess



													





			# window details
			
window = Tk()	# window is created
window.title("Brightness_Changer")	# a title is added to window
window.geometry("600x800")	# size of window id defined
window.configure(background="#111111")








			# widgets details
			

password_text = Label(window, text="Enter Your Password:")
password_guess = Entry(window, show="*")
password_guess.insert(0, "enter password")
password_text.pack()
password_guess.pack()


def medium():
    os.system('sudo ./brightness.sh --medium') 
    os.system('sleep(2)')
    print(password_guess.get()) 
btn=Button(window,text="medium",bg="#999999",command=medium)
btn.pack()

def slow():
    os.system('sudo ./brightness.sh --slow')
    os.system('sleep(2)')
    print(password_guess.get())
btn=Button(window,text="slow",bg="#999999",command=slow)
btn.pack()

def optimum():
    os.system('sudo ./brightness.sh -vvs')
    os.system('sleep(2)')
    print(password_guess.get())
btn=Button(window,text="optimum",bg="#999999",command=optimum)
btn.pack()




exit_button=Button(window,text="exit",bg="#888888",command=window.destroy)
exit_button.pack()











			# execution of window

window.mainloop()	# window is drawn





													
