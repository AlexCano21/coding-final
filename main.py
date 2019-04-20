##################################################################

# v v v    [Importing submodules]    v v v 

#Importing tk 
import tkinter
import tkinter as tk
from tkinter import tix
from tkinter import *
from tkinter.constants import *
root = tix.Tk()
from tkinter import Button 
root.title("Factory Game")

#Import time 
import time

#Importing call and random integer 
from subprocess import call
from random import randint  

##################################################################

#Clearing the command line
call('cls', shell=True)

##################################################################

# v v v    [Variables]    v v v 

#Stage: What stage you are at in your factory
with open('save.txt', 'r') as f:
	stage = f.readlines(1)
	pass

##################################################################

# v v v    [Commands]    v v v

#When this command is called it switches to the actual game
def switchToGame():
    #These two functions hide the title screen labels 
    titleLabel.pack_forget()
    authorsLabel.pack_forget()

    #Creating the leave button 
    leaveGame = Button(root, text="Leave Game", command=leaveGame)
    leaveGame.place(relx=0.85, rely=0.9, anchor="nw")

    root.configure(background='black')

def leaveGame():
    print("lol")

##################################################################

# v v v    [Making the intro screen]    v v v 

#Setting window wdith and heigth, and background color
root.geometry("500x300")
root.configure(background='black')

#Title Text
titleLabel = tk.Label(root, text='Factory Game', font=("Arial", 11), fg="white", bg="black")
titleLabel.place(relx=0.5, rely=0.4, anchor='center')
titleLabel.pack()

#Author Name Text
authorsLabel = tk.Label(root, text='By Alex C. and Benjamin B.', font=("Arial", 9), fg="white", bg="black")
authorsLabel.place(relx=0.5, rely=0.5, anchor='center')
authorsLabel.pack()

#Switches to the game screen by activating command
switchToGame()

##################################################################

#Mainloop: This keeps the window open
root.mainloop()