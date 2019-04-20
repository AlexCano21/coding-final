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

#Importing system commands
import sys

##################################################################

#Clearing the command line
call('cls', shell=True)

##################################################################

# v v v    [Variables]    v v v 

#This reads the save file and determines your progress
with open('save.txt', 'r') as f:
    #This is what stage you are on
    stage = f.readline()
    #This is how mush coal you have in your inventory
    coalInventory = f.readline()
    #This is how mush iron you have in your inventory
    ironInventory = f.readline()
    #This is how mush gold you have in your inventory
    goldInventory = f.readline()

#Removes the newline character from the read lines
coalInventory = coalInventory.strip("\n")
ironInventory = ironInventory.strip("\n")
goldInventory = goldInventory.strip("\n")

#Prints out your game state (this is for debugging purposes)
print("You are on stage: " + stage, end='')
print("You have " + coalInventory + " coal")
print("You have " + ironInventory + " iron")
print("You have " + goldInventory + " gold")

##################################################################

# v v v    [Commands]    v v v

#When this command is called it switches to the actual game
def switchToGame():
    #This defines the leaveGame function which is the command of the button in this screen
    def leaveGame():
        #Saves what stage you are in the game

        #Ends the python script
        sys.exit()

    #These two functions hide the title screen labels 
    titleLabel.place_forget()
    authorsLabel.place_forget()

    #Creating the leave button 
    leaveGame = Button(root, text="Leave Game", command=leaveGame)
    leaveGame.place(relx=0.85, rely=0.9, anchor="nw")

    root.configure(background='black')


##################################################################

# v v v    [Making the intro screen]    v v v 

#Setting window wdith and heigth, and background color
root.geometry("500x300")
root.configure(background='black')

#Title Text
titleLabel = tk.Label(root, text='Factory Game', font=("Arial", 11), fg="white", bg="black")
titleLabel.place(relx=0.5, rely=0.4, anchor='center')

#Author Name Text
authorsLabel = tk.Label(root, text='By Alex C. and Benjamin B.', font=("Arial", 9), fg="white", bg="black")
authorsLabel.place(relx=0.5, rely=0.5, anchor='center')

#Switches to the game screen by activating command
#switchToGame()

##################################################################

#Mainloop: This keeps the window open
root.mainloop()