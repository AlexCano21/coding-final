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
    #This is how mush copper you have in your inventory
    copperInventory = f.readline()
    pass

#This is how long the title screen stays up
titleScreenTime = 1500

#Removes the newline character from the read lines
coalInventory = coalInventory.strip("\n")
ironInventory = ironInventory.strip("\n")
copperInventory = copperInventory.strip("\n")

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
            global copperInventory
            #This makes all the save variables into strings
            coalInventory = str(coalInventory)
            ironInventory = str(ironInventory)
            copperInventory = str(copperInventory)
            #This writes to the save files
            f.write(stage)
            f.write(coalInventory + '\n')
            f.write(ironInventory + '\n')
            f.write(copperInventory + '\n')
            pass
          
        #Ends the python script
        sys.exit()
    
    
    #Update Items amount, minplu determines if minus or plus(1=minus, 2=plus)
    def updateCoal(minplu, amount):
        global coalInventory
        coalInventory = int(coalInventory)
        if minplu == 1:
            if amount < coalInventory:
                coalInventory = coalInventory - amount
            else:
                print("Temporary handling of not enough items")
        elif minplu == 2:
            coalInventory = coalInventory + amount
        else:
            print("Error 01")
        coalInventory = str(coalInventory)
        openInventory()
    def updateIron(minplu, amount):
        global ironInventory
        ironInventory = int(ironInventory)
        if minplu == 1:
            if amount < ironInventory:
                ironInventory = ironInventory - amount
            else:
                print("Temporary handling of not enough items")        
        elif minplu == 2:
            ironInventory = ironInventory + amount
        else:
            print("Error 01")
        ironInventory = str(ironInventory)
        openInventory()
    def updateCopper(minplu, amount):
        global copperInventory
        copperInventory = int(copperInventory)
        if minplu == 1:
            if amount < copperInventory:
                copperInventory = copperInventory - amount
            else:
                print("Temporary handling of not enough items")
        elif minplu == 2:
            copperInventory = copperInventory + amount
        else:
            print("Error 01")
        copperInventory = str(copperInventory)
        openInventory()
    

    #This command opens the inventory
    def openInventory():
        #This clears the command line
        call('cls', shell=True)

        #This prints what stage you are on and the inventory
        print("You are on stage: " + stage, end='')
        print("You have " + coalInventory + " coal")
        print("You have " + ironInventory + " iron")
        print("You have " + copperInventory + " copper")

    #This command opens the store
    def openStore():
        #This clears the command line
        call('cls', shell=True)

        #Prints the store
        print("Welcome to the store!")
    
    #Opening Crafting Interface
    def craftInterface():
        craft = tix.Tk()
        print(ironInventory)
        #Defining all Crafting Functions
        def craftIronGears():
            updateIron(1,4)
                        

        #Defining closing of Crafting Interface
        def closeWindow():
            craft.destroy()
        #Creating the close crafting button 
        leaveCrafting = Button(craft, text="Close Crafting Window", bg='black', fg='white', command=closeWindow)
        leaveCrafting.place(x=50, y=100)
        craftIronGear = Button(craft, text="Craft Iron Gear", bg='black', fg='white', command=craftIronGears)
        craftIronGear.place(x=50, y=50)
        craft.mainloop
    
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

    #Creating the Crafting button 
    craftInterface = Button(root, text="Crafting", bg='black', fg='white', command=craftInterface)
    craftInterface.place(x=100, y=270)

    #Buttons for testing out 
    addCoal = Button(root, text="Add Coal", bg='black', fg='white', command= lambda: updateCoal(2, 1))
    addIron = Button(root, text="Add Iron", bg='black', fg='white', command= lambda: updateIron(2, 1))
    addCopper = Button(root, text="Add Copper", bg='black', fg='white', command= lambda: updateCopper(2, 1))
    addCoal.place(x=100, y=100)
    addIron.place(x=100, y=130)
    addCopper.place(x=100, y=160)

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