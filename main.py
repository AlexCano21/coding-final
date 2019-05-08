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
import rnd as rnd
import random
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
# stage = int(data[0].strip("\n"), 10)
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
#how big the chance is that a random event occurs in a 10 cycles 1:chance --> 1:1000 
chance = 1

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
    val = int(data[0].strip("\n"), 10)
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
    data[0] = str(val) + "\n"
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
def updateIronGear(minplu, amount):
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
def updateRefinedCopper(minplu, amount):
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
def updateAdvCircuit(minplu, amount):
    with open('items.txt', 'r') as file:
        # read a list of lines into data
        data = file.readlines()
    val = int(data[9].strip("\n"), 10)
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
    data[9] = str(val) + "\n"
    with open('items.txt', 'w') as file:
        file.writelines( data ) 
def updateEngine(minplu, amount):
    with open('items.txt', 'r') as file:
        # read a list of lines into data
        data = file.readlines()
    val = int(data[10].strip("\n"), 10)
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
    data[10] = str(val) + "\n"
    with open('items.txt', 'w') as file:
        file.writelines( data ) 
def updateElectricEngine(minplu, amount):
    with open('items.txt', 'r') as file:
        # read a list of lines into data
        data = file.readlines()
    val = int(data[11].strip("\n"), 10)
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
    data[11] = str(val) + "\n"
    with open('items.txt', 'w') as file:
        file.writelines( data ) 
def updateProcessor(minplu, amount):
    with open('items.txt', 'r') as file:
        # read a list of lines into data
        data = file.readlines()
    val = int(data[12].strip("\n"), 10)
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
    data[12] = str(val) + "\n"
    with open('items.txt', 'w') as file:
        file.writelines( data ) 
def updateComputer(minplu, amount):
    with open('items.txt', 'r') as file:
        # read a list of lines into data
        data = file.readlines()
    val = int(data[13].strip("\n"), 10)
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
    data[13] = str(val) + "\n"
    with open('items.txt', 'w') as file:
        file.writelines( data ) 
def updateIronPlate(minplu, amount):
    with open('items.txt', 'r') as file:
        # read a list of lines into data
        data = file.readlines()
    val = int(data[14].strip("\n"), 10)
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
    data[14] = str(val) + "\n"
    with open('items.txt', 'w') as file:
        file.writelines( data ) 
def updateCopperPlate(minplu, amount):
    with open('items.txt', 'r') as file:
        # read a list of lines into data
        data = file.readlines()
    val = int(data[15].strip("\n"), 10)
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
    data[15] = str(val) + "\n"
    with open('items.txt', 'w') as file:
        file.writelines( data ) 
def updateSteelPlate(minplu, amount):
    with open('items.txt', 'r') as file:
        # read a list of lines into data
        data = file.readlines()
    val = int(data[16].strip("\n"), 10)
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
    data[16] = str(val) + "\n"
    with open('items.txt', 'w') as file:
        file.writelines( data ) 
def updateRefinedCopperPlate(minplu, amount):
    with open('items.txt', 'r') as file:
        # read a list of lines into data
        data = file.readlines()
    val = int(data[17].strip("\n"), 10)
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
    data[17] = str(val) + "\n"
    with open('items.txt', 'w') as file:
        file.writelines( data ) 


def openInventory():
    print(file_lengthy("items.txt"))
    for i in range(file_lengthy("items.txt")): 
        print(data[i].strip("\n"))

def buildingUpgrade(val):
    #different values are for different "upgrade stages" 
    if val == 1:
        if updateIronIngot(1, 100) != "error":
            if updateIronGear(1, 10) == "error":
                updateIronIngot(2, 100)
                return "error"
        else:
            return "error"
    elif val == 2:
        if updateCopperIngot(1, 100) != "error":
            if updateIronGear(1, 25) == "error":
                updateCopperIngot(2, 100)
                return "error"
            else:
                if updateCircuit(1, 20) == "error":
                    updateCopperIngot(2, 100)
                    updateIronGear(2, 25)
                    return "error"
        else:
            return "error"
    #elif val == 3:

    #elif val == 4:

    #elif val == 5:

    #elif val == 6:

    #elif val == 7:

    #elif val == 8:

    #elif val == 9:

    #elif val == 10:

    #elif val == 11:

    #elif val == 12:

    #elif val == 13:

    #elif val == 14:

    #elif val == 15:


#When this command is called it switches to the actual game
def switchToGame():
    #This defines the leaveGame function which is the command of the button in this screen
    #This command opens the store
    def openStore():
        #This clears the command line
        call('cls', shell=True)

        #Prints the store
        print("Welcome to the store!")
    
    #This places the new generators and tracks
    def addBfurnace1():
        bfurnaceLevel1 = PhotoImage(file="blastfurnace1.png")
        bfurnaceLvl1Label = Label(root, borderwidth="0", image=bfurnaceLevel1)
        bfurnaceLvl1Label.image = bfurnaceLevel1
        bfurnaceLvl1Label.place(x=201, y=35)
        blastFurnace1.place_forget()
    def addCopperOne():
        def addCopperTwo():
            def addCopperThree():
                def addCopperFour():
                    def addCopperFive():
                        copperLevel5 = PhotoImage(file="copper5.png")
                        copperLvl5Label = Label(root, borderwidth="0", image=copperLevel5)
                        copperLvl5Label.image = copperLevel5
                        copperLvl5Label.place(x=15, y=179)
                        copper5.place_forget()
                    copperLevel4 = PhotoImage(file="copper4.png")
                    copperLvl4Label = Label(root, borderwidth="0", image=copperLevel4)
                    copperLvl4Label.image = copperLevel4
                    copperLvl4Label.place(x=15, y=179)
                    copper4.place_forget()
                    copper5 = Button(root, text="Add Copper level 5", bg='black', fg='white', command=addCopperFive)
                    copper5.place(x=258, y=218)
                copperLevel3 = PhotoImage(file="copper3.png")
                copperLvl3Label = Label(root, borderwidth="0", image=copperLevel3)
                copperLvl3Label.image = copperLevel3
                copperLvl3Label.place(x=15, y=179)
                copper3.place_forget()
                copper4 = Button(root, text="Add Copper level 4", bg='black', fg='white', command=addCopperFour)
                copper4.place(x=258, y=218)
            copperLevel2 = PhotoImage(file="copper2.png")
            copperLvl2Label = Label(root, borderwidth="0", image=copperLevel2)
            copperLvl2Label.image = copperLevel2
            copperLvl2Label.place(x=15, y=179)
            copper2.place_forget()
            copper3 = Button(root, text="Add Copper level 3", bg='black', fg='white', command=addCopperThree)
            copper3.place(x=258, y=218)
        copperLevel1 = PhotoImage(file="copper1.png")
        copperLvl1Label = Label(root, borderwidth="0", image=copperLevel1)
        copperLvl1Label.image = copperLevel1
        copperLvl1Label.place(x=23, y=147)
        copper1.place_forget()
        copper2 = Button(root, text="Add Copper level 2", bg='black', fg='white', command=addCopperTwo)
        copper2.place(x=258, y=218)
    def addFuranceTwo():
        def addCopperOne():
            def addCopperTwo():
                def addCopperThree():
                    def addCopperFour():
                        def addCopperFive():
                            copperLevel5 = PhotoImage(file="copper5.png")
                            copperLvl5Label = Label(root, borderwidth="0", image=copperLevel5)
                            copperLvl5Label.image = copperLevel5
                            copperLvl5Label.place(x=15, y=179)
                            copper5.place_forget()
                        copperLevel4 = PhotoImage(file="copper4.png")
                        copperLvl4Label = Label(root, borderwidth="0", image=copperLevel4)
                        copperLvl4Label.image = copperLevel4
                        copperLvl4Label.place(x=15, y=179)
                        copper4.place_forget()
                        copper5 = Button(root, text="Add Copper level 5", bg='black', fg='white', command=addCopperFive)
                        copper5.place(x=258, y=218)
                    copperLevel3 = PhotoImage(file="copper3.png")
                    copperLvl3Label = Label(root, borderwidth="0", image=copperLevel3)
                    copperLvl3Label.image = copperLevel3
                    copperLvl3Label.place(x=15, y=179)
                    copper3.place_forget()
                    copper4 = Button(root, text="Add Copper level 4", bg='black', fg='white', command=addCopperFour)
                    copper4.place(x=258, y=218)
                copperLevel2 = PhotoImage(file="copper2.png")
                copperLvl2Label = Label(root, borderwidth="0", image=copperLevel2)
                copperLvl2Label.image = copperLevel2
                copperLvl2Label.place(x=15, y=179)
                copper2.place_forget()
                copper3 = Button(root, text="Add Copper level 3", bg='black', fg='white', command=addCopperThree)
                copper3.place(x=258, y=218)
            copperLevel1 = PhotoImage(file="copper1.png")
            copperLvl1Label = Label(root, borderwidth="0", image=copperLevel1)
            copperLvl1Label.image = copperLevel1
            copperLvl1Label.place(x=23, y=147)
            copperText = PhotoImage(file="copperlabel.png")
            copperLabel = Label(root, borderwidth="0", image=copperText)
            copperLabel.image = copperText
            copperLabel.place(x=357, y=123)
            copper1.place_forget()
            copper2 = Button(root, text="Add Copper level 2", bg='black', fg='white', command=addCopperTwo)
            copper2.place(x=258, y=218)
        furnaceLevel2 = PhotoImage(file="furnace2.png")
        furnaceLvl2Label = Label(root, borderwidth="0", image=furnaceLevel2)
        furnaceLvl2Label.image = furnaceLevel2
        furnaceLvl2Label.place(x=193, y=97)
        furnace2out1 = PhotoImage(file="furnace2out1.png")
        furnace2out1Label = Label(root, borderwidth="0", image=furnace2out1)
        furnace2out1Label.image = furnace2out1
        furnace2out1Label.place(x=331, y=99)
        furnace2.place_forget()
        copper1 = Button(root, text="Add Copper level 1", bg='black', fg='white', command=addCopperOne)
        copper1.place(x=258, y=218)
    def addCoalTwo():
        def addCoalThree():
            def addCoalFour():
                def addCoalFive():
                    coalLevel5 = PhotoImage(file="coal5.png")
                    coalLvl5Label = Label(root, borderwidth="0", image=coalLevel5)
                    coalLvl5Label.image = coalLevel5
                    coalLvl5Label.place(x=31, y=19)
                    coal5.place_forget()
                coalLevel4 = PhotoImage(file="coal4.png")
                coalLvl4Label = Label(root, borderwidth="0", image=coalLevel4)
                coalLvl4Label.image = coalLevel4
                coalLvl4Label.place(x=31, y=19)
                coal4.place_forget()
                coal5 = Button(root, text="Add Coal level 5", bg='black', fg='white', command=addCoalFive)
                coal5.place(x=350, y=244)
            coalLevel3 = PhotoImage(file="coal3.png")
            coalLvl3Label = Label(root, borderwidth="0", image=coalLevel3)
            coalLvl3Label.image = coalLevel3
            coalLvl3Label.place(x=31, y=19)
            coal3.place_forget()
            coal4 = Button(root, text="Add Coal level 4", bg='black', fg='white', command=addCoalFour)
            coal4.place(x=350, y=244)
        #This puts the level 2 iron generator over the first one
        coalLevel2 = PhotoImage(file="coal2.png")
        coalLvl2Label = Label(root, borderwidth="0", image=coalLevel2)
        coalLvl2Label.image = coalLevel2
        coalLvl2Label.place(x=31, y=19)
        #Adds the new button
        coal2.place_forget()
        coal3 = Button(root, text="Add Coal level 3", bg='black', fg='white', command=addCoalThree)
        coal3.place(x=350, y=244)
        
    def addIronTwo():
        def addIronThree():
            def addIronFour():
                def addIronFive():
                    ironLevel5 = PhotoImage(file="iron5.png")
                    ironLvl5Label = Label(root, borderwidth="0", image=ironLevel5)
                    ironLvl5Label.image = ironLevel5
                    ironLvl5Label.place(x=11, y=90)
                    iron5.place_forget()
                ironLevel4 = PhotoImage(file="iron4.png")
                ironLvl4Label = Label(root, borderwidth="0", image=ironLevel4)
                ironLvl4Label.image = ironLevel4
                ironLvl4Label.place(x=11, y=91)
                iron4.place_forget()
                iron5 = Button(root, text="Add Iron level 5", bg='black', fg='white', command=addIronFive)
                iron5.place(x=254, y=244)
            ironLevel3 = PhotoImage(file="iron3.png")
            ironLvl3Label = Label(root, borderwidth="0", image=ironLevel3)
            ironLvl3Label.image = ironLevel3
            ironLvl3Label.place(x=12, y=93)
            iron3.place_forget()
            iron4 = Button(root, text="Add Iron level 4", bg='black', fg='white', command=addIronFour)
            iron4.place(x=258, y=244)
        #This puts the level 2 iron generator over the first one
        ironLevel2 = PhotoImage(file="iron2.png")
        ironLvl2Label = Label(root, borderwidth="0", image=ironLevel2)
        ironLvl2Label.image = ironLevel2
        ironLvl2Label.place(x=19, y=98)
        #Adds the new button
        iron2.place_forget()
        iron3 = Button(root, text="Add Iron level 3", bg='black', fg='white', command=addIronThree)
        iron3.place(x=258, y=244)

    def upgradeFurnace():
        with open('buildings.txt', 'r') as file:
            data = file.readlines()
        frnlvl = int(data[3].strip("\n"), 10)
        if buildingUpgrade(frnlvl) != "error":
            frnlvl = frnlvl + 1
            data[14] = str(frnlvl) + "\n"
            with open('buildings.txt', 'w') as file:
                file.writelines( data )
    
    #Opening Crafting Interface
    def craftInterface():
        craft = tix.Tk()
        #Defining all Crafting Functions
        def craftIronGears():
            #taking of 4 iron ingots if no error is returned
            if updateIronIngot(1,4) != "error":
                #adding one iron gear
                updateIronGear(2,1)
            else:
                #if not enough iron is available an error is thrown. This will probably be replaced by a nice visual in the game window
                print("Error 02: Not enought items")
        def craftCircuit():
            if updateCopperIngot(1,3) != "error":
                updateCircuit(2,1)
            else:
                print("Error 02: Not enough items")                        
        def craftAdvCircuit():
            if updateRefinedCopper(1,3) != "error":
                updateAdvCircuit(2,1)
            else:
                print("Error 02: Not enough items")
        def craftIronPlate():
            if updateIronIngot(1,2) != "error":
                updateIronPlate(2,1)
            else:
                print("Error 02: Not enough items")
        def craftSteelIngot():
            if updateSteelIngot(1,2) != "error":
                updateSteelPlate(2,1)
            else:
                print("Error 02: Not enough items")
        def craftCopperPlate():
            if updateCopperIngot(1,2) != "error":
                updateCopperPlate(2,1)
            else:
                print("Error 02: Not enough items")
        def craftRefinedCopperPlate():
            if updateRefinedCopper(1,2) != "error":
                updateRefinedCopperPlate(2,1)
            else:
                print("Error 02: Not enough items")
        def craftEngine():
            #taking 5 iron plate if possible(no error)
            if updateIronPlate(1,5) != "error":
                #taking 2 steel plates if possible
                if updateSteelPlate(1,2) != "error":
                    #if enough of both are available one engine is added to the inventory
                    updateEngine(2,1)
                else:
                    #if there are not enough steel plates you get the iron plates back
                    updateIronPlate(2,5)
                    print("Error 02: Not enough items")
            else:
                print("Error 02: Not enough items")
        def craftElectricEngine():
            if updateEngine(1,1) != "error":
                if updateCircuit(1,5) != "error":
                    updateElectricEngine(2,1)
                else:
                    updateEngine(2,1)
                    print("Error 02: Not enough items")
            else:
                print("Error 02: Not enough items")
        def craftProcessor():
            if updateAdvCircuit(1,2) != "error":
                if updateCircuit(1,5) != "error":
                    updateProcessor(2,1)
                else:
                    updateAdvCircuit(2,2)
                    print("Error 02: Not enough items")
            else:
                print("Error 02: Not enough items")
        def craftComputer():
            if updateProcessor(1,2) != "error":
                if updateIronPlate(1,4) != "error":
                    updateComputer(2,1)
                else:
                    updateProcessor(2,2)
                    print("Error 02: Not enough items")
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

    #Displaying the factory (This will be the main screen)
    mainScreen = PhotoImage(file="stage0.png")
    mainLabel = Label(root, bg="black", image=mainScreen)
    mainLabel.image = mainScreen
    mainLabel.place(x=0, y=0)

    #This is for testing out the graphics
    iron2 = Button(root, text="Add Iron level 2", bg='black', fg='white', command=addIronTwo)
    iron2.place(x=258, y=244)
    coal2 = Button(root, text="Add Coal level 2", bg='black', fg='white', command=addCoalTwo)
    coal2.place(x=350, y=244)
    furnace2 = Button(root, text="Add Furnace level 2", bg='black', fg='white', command=addFuranceTwo)
    furnace2.place(x=450, y=244)
    blastFurnace1 = Button(root, text="Add Blast Furnace level 1", bg='black', fg='white', command=addBfurnace1)
    blastFurnace1.place(x=258, y=200)

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

#picking a random event
def randomEvent():
    rndNumber = random.randint(0, 6)
    if rndNumber == 1:
        rnd.workerStrike()
    elif rndNumber == 2:
        rnd.factoryFire()
    elif rndNumber == 3:
        rnd.worldWar()
    elif rndNumber == 4:
        rnd.theGreatDepression()
    elif rndNumber == 5:
        rnd.theSnap()
    elif rndNumber == 6:
        rnd.elonInvests()



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
        elif x%10 == 0:
            print(chance)
            rndnr = random.randint(0, chance)
            if rndnr <= 1:
                randomEvent()
        if p1.is_alive() == False:
            break

#Furnace Timer
def furnaceTimer():
    with open('buildings.txt', 'r') as file:
        data = file.readlines()
    furnaceLevel = int(data[3].strip("\n"), 10)
    updateIron(1, ironSmeltRate*furnaceLevel)
    updateCoal(1, coalSmeltRate*furnaceLevel)
    updateIronIngot(2, ironSmeltRate*furnaceLevel)
    if furnaceLevel >= 2:
        updateCopper(1, copperSmeltRate*furnaceLevel)
        updateCopperIngot(2, copperSmeltRate*furnaceLevel)
        updateCoal(1, coalSmeltRate*furnaceLevel)
        
if __name__=='__main__':
    p1 = Process(target=loop)
    p1.start()
    p2 = Process(target=spawnerTimer())
    p2.start()
    p1.join()
    p2.join()    