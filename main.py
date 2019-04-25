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
    pass

#This is how long the title screen stays up
titleScreenTime = 1500

#Removes the newline character from the read lines
coalInventory = coalInventory.strip("\n")
ironInventory = ironInventory.strip("\n")
goldInventory = goldInventory.strip("\n")

##################################################################

# v v v    [Commands]    v v v

#When this command is called it switches to the actual game
def switchToGame():
    #This defines the leaveGame function which is the command of the button in this screen
    def leaveGame():
        #Saves what stage you are in the game
        with open('save.txt', 'w') as f:
            #This makes all the saveable variables global 
            global coalInventory
            global ironInventory
            global goldInventory
            #This makes all the save variables into strings
            coalInventory = str(coalInventory)
            ironInventory = str(ironInventory)
            goldInventory = str(goldInventory)
            #This writes to the save files
            f.write(stage)
            f.write(coalInventory + '\n')
            f.write(ironInventory + '\n')
            f.write(goldInventory + '\n')
            pass
          
        #Ends the python script
        sys.exit()

    #All of these commands are for the testing buttons
    def addCoal():
        global coalInventory
        coalInventory = int(coalInventory)
        coalInventory = coalInventory + 1
        coalInventory = str(coalInventory)
        openInventory()
    def addIron():
        global ironInventory
        ironInventory = int(ironInventory)
        ironInventory = ironInventory + 1
        ironInventory = str(ironInventory)
        openInventory()
    def addGold():
        global goldInventory
        goldInventory = int(goldInventory)
        goldInventory = goldInventory + 1
        goldInventory = str(goldInventory)
        openInventory()

    #This command opens the inventory
    def openInventory():
        #This clears the command line
        call('cls', shell=True)

        #This prints what stage you are on and the inventory
        print("You are on stage: " + stage, end='')
        print("You have " + coalInventory + " coal")
        print("You have " + ironInventory + " iron")
        print("You have " + goldInventory + " gold")

    #This command opens the store
    def openStore():
        #This clears the command line
        call('cls', shell=True)

        #Prints the store
        print("Welcome to the store!")
    
    #These two functions hide the title screen labels 
    titleLabel.place_forget()
    authorsLabel.place_forget()

    #This makes the buttton to open inventory
    openCommand = Button(root, text="Open inventory", bg='black', fg='white', command=openInventory)
    openCommand.place(x=330, y=270)

    #This makes the button to open store
    openStore = Button(root, text="Open Store", bg='black', fg='white', command=openStore)
    openStore.place(x=258, y=270)

    #Creating the leave button 
    leaveGame = Button(root, text="Leave Game", bg='black', fg='white', command=leaveGame)
    leaveGame.place(x=425, y=270)

    #Buttons for testing out 
    addCoal = Button(root, text="Add Coal", bg='black', fg='white', command=addCoal)
    addIron = Button(root, text="Add Iron", bg='black', fg='white', command=addIron)
    addGold = Button(root, text="Add Gold", bg='black', fg='white', command=addGold)
    addCoal.place(x=100, y=100)
    addIron.place(x=100, y=130)
    addGold.place(x=100, y=160)

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

#Switches to the game screen by activating command after time on titleScreenTime variable passes
titleLabel.after(titleScreenTime, switchToGame)

##################################################################

#Mainloop: This keeps the window open
root.mainloop()