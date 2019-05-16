import tkinter as tk
from PIL import Image

#This creates the main window of an application
window = tk.Tk()
window.title("Join")
window.geometry("300x300")
window.configure(background='grey')

path = "Aaron.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "bottom", fill = "both", expand = "yes")

#Start the GUI
window.mainloop()

#######################################################################################################################################
#######################################################################################################################################

#This places the new generators and tracks
    def addBfurnace1():
        bfurnaceLevel1 = PhotoImage(file="blastfurnace1.png")
        bfurnaceLvl1Label = Label(root, borderwidth="0", image=bfurnaceLevel1)
        bfurnaceLvl1Label.image = bfurnaceLevel1
        bfurnaceLvl1Label.place(x=201, y=35)
        blastFurnace1.place_forget()
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