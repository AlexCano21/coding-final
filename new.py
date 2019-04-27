##################################################################

# v v v    [Importing submodules]    v v v 

#Importing tk 
import tkinter
import tkinter as tk
from tkinter import tix
from tkinter import *
from tkinter.constants import *
from tkinter import Button 


import time


from multiprocessing import Process

#Import time 
import time

#Importing call and random integer 
from subprocess import call
from random import randint  

#Importing system commands
import sys


root = tix.Tk()
root.title("Factory Game")

#Getting length of save file
def file_lengthy(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1


#Reading Saved Game
with open('items.txt', 'r') as file:
    # read a list of lines into data
    data = file.readlines()
##################################################################

#Clearing the command line
call('cls', shell=True)

##################################################################


#Balancing/Global Variables
#current stage
stage = int(data[0].strip("\n"), 10)
#counter variable
x = 0
#how long inbetween spawning cycles in seconds
freq = 1
#Difficulty 1 normal higher easier smaller more difficult (0.25, 0.5, 0.75, 1, 2, 3, 4...)
diff = 2
#rarity of Iron Ore
ironRar = 2
#rarity of Coal Ore
coalRar = 3
#rarity of Copper Ore
copperRar = 1
#Iron Spawned in 1 cycle
ironSpawnRate = round(diff*ironRar)
#Coal Spawned in 1 cycle
coalSpawnRate = round(diff*coalRar)
#Copper Spawned in 1 cycle
copperSpawnRate = round(diff*copperRar)
#Furnace Level: Hardcoded for now will be in save game later
frnlvl = 1
#Copper smelting in 1 cycle
copperSmeltRate = round(diff)
#Iron smelting in 1 cycle
ironSmeltRate = round(diff*2)
#Coal usage for normal furnace in 1 cycle
coalSmeltRate = round(diff*4)

##################################################################

#This is how long the title screen stays up
titleScreenTime = 1500

#All the updating functions, only one will be fully commented out
def updateIronIngot(minplu, amount):
    #minplu determines if there will be a subtractin or addidtion opperation perfmormed(1 = -   2 = +)
    #amount is the amount that will be added/subtracted
    #opening the gamefile
    with open('items.txt', 'r') as file:
        #reading data of the file and saving it in a variable --> data
        data = file.readlines()
    #extreacting the number by getting rid of the \n and converting it into and integer with base 10
    val = int(data[4].strip("\n"), 10)
    #if minplu is 1 it goes down the subtraction path
    if minplu == 1:
        #this is checking if the value that it is trying to subtract is not bigger than the available resources
        if amount <= val:
            #if the val is smaller or equal the subtraction is carried out
            val = val - amount
        else:
            #if not it returns error which in turn will display that there are not enough items
            return "error"   
    #if minplu is 2 it will go down the addidtion path 
    elif minplu == 2:
        #it get added
        val = val + amount
    else:
        #incase that something with the input is wrong an error will be displayed
        print("Error 01")
    #Here the newly calculated data gets converted to a string and added back into data
    data[4] = str(val) + "\n"
    #Here the file gets opened once again this time in write mode (w)
    with open('items.txt', 'w') as file:
        #now the file gets overwritten with the new data
        file.writelines( data ) 

def updateIron(minplu, amount):
    with open('items.txt', 'r') as file:
        # read a list of lines into data
        data = file.readlines()
    val = int(data[2].strip("\n"), 10)
    if minplu == 1:
        if amount <= val:
            val = val - amount
        else:
            return "error"      
    elif minplu == 2:
        val = val + amount
    else:
        print("Error 01")
    print(val)
    data[2] = str(val) + "\n"
    with open('items.txt', 'w') as file:
        file.writelines( data ) 

def updateCoal(minplu, amount):
    with open('items.txt', 'r') as file:
        # read a list of lines into data
        data = file.readlines()
    val = int(data[1].strip("\n"), 10)
    if minplu == 1:
        if amount <= val:
            val = val - amount
        else:
            return "error"      
    elif minplu == 2:
        val = val + amount
    else:
        print("Error 01")
    print(val)
    data[1] = str(val) + "\n"
    with open('items.txt', 'w') as file:
        file.writelines( data ) 

def updateCopper(minplu, amount):
    with open('items.txt', 'r') as file:
        # read a list of lines into data
        data = file.readlines()
    val = int(data[3].strip("\n"), 10)
    if minplu == 1:
        if amount <= val:
            val = val - amount
        else:
            return "error"       
    elif minplu == 2:
        val = val + amount
    else:
        print("Error 01")
    print(val)
    data[3] = str(val) + "\n"
    with open('items.txt', 'w') as file:
        file.writelines( data ) 

def updateIronGear(minplu, amount):
    with open('items.txt', 'r') as file:
        # read a list of lines into data
        data = file.readlines()
    val = int(data[6].strip("\n"), 10)
    if minplu == 1:
        if amount <= val:
            val = val - amount
        else:
            return "error"       
    elif minplu == 2:
        val = val + amount
    else:
        print("Error 01")
    print(val)
    data[6] = str(val) + "\n"
    with open('items.txt', 'w') as file:
        file.writelines( data ) 

def updateCopperIngot(minplu, amount):
    with open('items.txt', 'r') as file:
        # read a list of lines into data
        data = file.readlines()
    val = int(data[5].strip("\n"), 10)
    if minplu == 1:
        if amount <= val:
            val = val - amount
        else:
            return "error"      
    elif minplu == 2:
        val = val + amount
    else:
        print("Error 01")
    print(val)
    data[5] = str(val) + "\n"
    with open('items.txt', 'w') as file:
        file.writelines( data ) 

def updateCircuit(minplu, amount):
    with open('items.txt', 'r') as file:
        # read a list of lines into data
        data = file.readlines()
    val = int(data[8].strip("\n"), 10)
    if minplu == 1:
        if amount <= val:
            val = val - amount
        else:
            return "error"     
    elif minplu == 2:
        val = val + amount
    else:
        print("Error 01")
    print(val)
    data[8] = str(val) + "\n"
    with open('items.txt', 'w') as file:
        file.writelines( data ) 

def updateSteelIngot(minplu, amount):
    with open('items.txt', 'r') as file:
        # read a list of lines into data
        data = file.readlines()
    val = int(data[7].strip("\n"), 10)
    if minplu == 1:
        if amount <= val:
            val = val - amount
        else:
            return "error"     
    elif minplu == 2:
        val = val + amount
    else:
        print("Error 01")
    print(val)
    data[7] = str(val) + "\n"
    with open('items.txt', 'w') as file:
        file.writelines( data ) 


def openInventory():
    print(file_lengthy("items.txt"))
    for i in range(file_lengthy("items.txt")): 
        print(data[i].strip("\n"))


#When this command is called it switches to the actual game
def switchToGame():
    #This defines the leaveGame function which is the command of the button in this screen
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
        
        def craftCircuit():
            if updateCopperIngot(1,3) != "error":
                updateCircuit(2,1)
            else:
                print("Error 02: Not enough items")                        
    
        #Defining closing of Crafting Interface
        def closeWindow():
            craft.destroy()
        #Creating the close crafting button 
        leaveCrafting = Button(craft, text="Close Crafting Window", bg='black', fg='white', command=closeWindow)
        leaveCrafting.place(x=50, y=100)
        craftIronGear = Button(craft, text="Craft Iron Gear", bg='black', fg='white', command=craftIronGears)
        craftIronGear.place(x=50, y=50)
        craftCircuit = Button(craft, text="Craft Circuit", bg='black', fg='white', command=craftCircuit)
        craftCircuit.place(x=50, y=25)
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
    
    #Leave game function
    def leave():
        sys.exit()

    #Creating the leave button 
    leaveGame = Button(root, text="Leave Game", bg='black', fg='white', command=leave)
    leaveGame.place(x=425, y=270)
    
    #Creating the Crafting button 
    craftInterface = Button(root, text="Crafting", bg='black', fg='white', command=craftInterface)
    craftInterface.place(x=100, y=270)

    #Buttons for testing out currently commented out because they are currently not needed
    #addCoal = Button(root, text="Add Coal", bg='black', fg='white', command= lambda: updateCoal(2, 1))
    #addIron = Button(root, text="Add Iron", bg='black', fg='white', command= lambda: updateIron(2, 1))
    #addCopper = Button(root, text="Add Copper", bg='black', fg='white', command= lambda: updateCopper(2, 1))
    #addCoal.place(x=100, y=100)
    #addIron.place(x=100, y=130)
    #addCopper.place(x=100, y=160)

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

#mainloop running
def loop():
    root.mainloop()


#Background Process Timer
def spawnerTimer():
    x = 0
    while True:
        x = x +1
        time.sleep(freq)
        with open('buildings.txt', 'r') as file:
            data = file.readlines()
        coalSpawner = int(data[0].strip("\n"), 10)
        ironSpawner = int(data[1].strip("\n"), 10)
        copperSpawner = int(data[2].strip("\n"), 10)
        updateIron(2, ironSpawnRate*ironSpawner)
        updateCoal(2, coalSpawnRate*coalSpawner)
        updateCopper(2, copperSpawnRate*copperSpawner)
        if x%4 == 0:
            furnaceTimer()
        if p1.is_alive() == False:
            break

#Furnace Timer
def furnaceTimer():
    with open('buildings.txt', 'r') as file:
        data = file.readlines()
    furnaceLevel = int(data[3].strip("\n"), 10)
    updateIron(1, ironSmeltRate*furnaceLevel)
    updateCoal(1, coalSmeltRate*furnaceLevel)
    updateCopper(1, copperSmeltRate*furnaceLevel)
    updateCopperIngot(2, copperSmeltRate*furnaceLevel)
    updateIronIngot(2, ironSmeltRate*furnaceLevel)
        
if __name__=='__main__':
    p1 = Process(target=loop)
    p1.start()
    p2 = Process(target=spawnerTimer())
    p2.start()
    p1.join()
    p2.join()    