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
    #This is how mush iron ingots you have in your inventory
    ironIngotInventory = f.readline()
    #This is how mush copper ingots you have in your inventory
    copperIngotInventory = f.readline()
    #This is how mush iron gears you have in your inventory
    ironGearInventory = f.readline()
    #This is how mush steel ingots you have in your inventory
    steelIngotInventory = f.readline()
    #This is how mush circuits you have in your inventory
    circuitInventory = f.readline()
    #This is how mush advanced circuits you have in your inventory
    advCircuitInventory = f.readline()
    #This is how mush refined copper you have in your inventory
    refinedCopperInventory = f.readline()
    #This is how mush engines you have in your inventory
    engineInventory = f.readline()
    #This is how mush electric engines you have in your inventory
    electricEngineInventory = f.readline()
    #This is how mush processors you have in your inventory
    processorInventory = f.readline()
    #This is how mush computers you have in your inventory
    computerInventory = f.readline()
    #This is how mush iron plates you have in your inventory
    ironPlateInventory = f.readline()
    #This is how mush copper plates you have in your inventory
    copperPlateInventory = f.readline()
    #This is how mush steel plates you have in your inventory
    steelPlateInventory = f.readline()
    #This is how mush refined copper plates you have in your inventory
    refinedCopperPlateInventory = f.readline()

    pass

#This is how long the title screen stays up
titleScreenTime = 1500

#Removes the newline character from the read lines
coalInventory = coalInventory.strip("\n")
ironInventory = ironInventory.strip("\n")
copperInventory = copperInventory.strip("\n")
ironIngotInventory = ironIngotInventory.strip("\n")
copperIngotInventory = copperIngotInventory.strip("\n")
ironGearInventory = ironGearInventory.strip("\n")
steelIngotInventory = steelIngotInventory.strip("\n")
circuitInventory = circuitInventory.strip("\n")
advCircuitInventory = advCircuitInventory.strip("\n")
refinedCopperInventory = refinedCopperInventory.strip("\n")
engineInventory = engineInventory.strip("\n")
electricEngineInventory = electricEngineInventory.strip("\n")
processorInventory = processorInventory.strip("\n")
computerInventory = computerInventory.strip("\n")
ironPlateInventory = ironPlateInventory.strip("\n")
copperPlateInventory = copperPlateInventory.strip("\n")
steelPlateInventory = steelPlateInventory.strip("\n")
refinedCopperPlateInventory = refinedCopperPlateInventory.strip("\n")

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
            global ironIngotInventory
            global copperIngotInventory
            global ironGearInventory
            global steelIngotInventory
            global circuitInventory
            global advCircuitInventory
            global refinedCopperInventory
            global engineInventory
            global electricEngineInventory
            global processorInventory
            global computerInventory
            global ironPlateInventory
            global copperPlateInventory
            global steelPlateInventory
            global refinedCopperPlateInventory
            #This makes all the save variables into strings
            coalInventory = str(coalInventory)
            ironInventory = str(ironInventory)
            copperInventory = str(copperInventory)
            ironIngotInventory = str(ironIngotInventory)
            copperIngotInventory = str(copperIngotInventory)
            ironGearInventory = str(ironGearInventory)
            steelIngotInventory = str(steelIngotInventory)
            circuitInventory = str(circuitInventory)
            advCircuitInventory = str(advCircuitInventory)
            refinedCopperInventory = str(refinedCopperInventory)
            engineInventory = str(engineInventory)
            electricEngineInventory = str(electricEngineInventory)
            processorInventory = str(processorInventory)
            computerInventory = str(computerInventory)
            ironPlateInventory = str(ironPlateInventory)
            copperPlateInventory = str(copperPlateInventory)
            steelPlateInventory = str(steelPlateInventory)
            refinedCopperPlateInventory = str(refinedCopperPlateInventory)
            #This writes to the save files
            f.write(stage)
            f.write(coalInventory + '\n')
            f.write(ironInventory + '\n')
            f.write(copperInventory + '\n')
            f.write(ironIngotInventory + '\n')
            f.write(copperIngotInventory + '\n')
            f.write(ironGearInventory + '\n')
            f.write(steelIngotInventory + '\n')
            f.write(circuitInventory + '\n')
            f.write(advCircuitInventory + '\n')
            f.write(refinedCopperInventory + '\n')
            f.write(engineInventory + '\n')
            f.write(electricEngineInventory + '\n')
            f.write(processorInventory + '\n')
            f.write(computerInventory + '\n')
            f.write(ironPlateInventory + '\n')
            f.write(copperPlateInventory + '\n')
            f.write(steelPlateInventory + '\n')
            f.write(refinedCopperPlateInventory + '\n')
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
                coalInventory = str(coalInventory)
                return "error"
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
                ironInventory = str(ironInventory)
                return "error"        
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
                copperInventory = str(copperInventory)
                return "error"
        elif minplu == 2:
            copperInventory = copperInventory + amount
        else:
            print("Error 01")
        copperInventory = str(copperInventory)
        openInventory()
    def updateIronIngot(minplu, amount):
        global ironIngotInventory
        ironIngotInventory = int(ironIngotInventory)
        if minplu == 1:
            if amount <= ironIngotInventory:
                ironIngotInventory = ironIngotInventory - amount
            else:
                ironIngotInventory = str(ironIngotInventory)
                return "error"        
        elif minplu == 2:
            ironIngotInventory = ironIngotInventory + amount
        else:
            print("Error 01")
        ironIngotInventory = str(ironIngotInventory)
        openInventory()
    def updateCopperIngot(minplu, amount):
        global copperIngotInventory
        copperIngotInventory = int(copperIngotInventory)
        if minplu == 1:
            if amount < copperIngotInventory:
                copperIngotInventory = copperIngotInventory - amount
            else:
                copperIngotInventory = str(copperIngotInventory)
                return "error"        
        elif minplu == 2:
            copperIngotInventory = copperIngotInventory + amount
        else:
            print("Error 01")
        copperIngotInventory = str(copperIngotInventory)
        openInventory()
    def updateIronGear(minplu, amount):
        global ironGearInventory
        ironGearInventory = int(ironGearInventory)
        if minplu == 1:
            if amount < ironGearInventory:
                ironGearInventory = ironGearInventory - amount
            else:
                ironGearInventory = str(ironGearInventory)
                return "error"       
        elif minplu == 2:
            ironGearInventory = ironGearInventory + amount
        else:
            print("Error 01")
        ironGearInventory = str(ironGearInventory)
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
        print("You have " + ironIngotInventory + " iron ingots")
        print("You have " + copperIngotInventory + " copper ingots")
        print("You have " + ironGearInventory + " iron gears")
        print("You have " + steelIngotInventory + " steel ingots")
        print("You have " + circuitInventory + " circuits")
        print("You have " + advCircuitInventory + " advanced circuits")
        print("You have " + refinedCopperInventory + " refined copper")
        print("You have " + engineInventory + " engines")
        print("You have " + electricEngineInventory + " electric engines")
        print("You have " + processorInventory + " processors")
        print("You have " + computerInventory + " computers")
        print("You have " + ironPlateInventory + " iron plates")
        print("You have " + copperPlateInventory + " copper plates")
        print("You have " + steelPlateInventory + " steel plates")
        print("You have " + refinedCopperPlateInventory + " refined copper plates")

    #This command opens the store
    def openStore():
        #This clears the command line
        call('cls', shell=True)

        #Prints the store
        print("Welcome to the store!")
    
    #Opening Crafting Interface
    def craftInterface():
        craft = tix.Tk()
        #Defining all Crafting Functions
        def craftIronGears():
            if updateIronIngot(1,4) != "error":
                updateIronGear(2,1)
            else:
                print("Error 02: Not enought items")
                        

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