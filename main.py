#Importing submodules 
from graphics import *
import time
from subprocess import call
from random import randint  

#Clearing the command line
call('cls', shell=True)

#Variables
greetingText="Hello, welcome to [Name Goes Here]!"
x=0
y=0

#Making the first Screen
def main():
    #Makes the window pop up with a name, and how large in pixels it is (width, height)
    win = GraphWin("[Name Goes Here]", 500, 400)
    #Set Background
    win.setBackground(color_rgb(255,255,255))

    #Calls Image
    homeImage = Image(Point(0,0), "blank.png")
    homeImage.draw(win)

    #Displays the greeting text
    greeting = Text(Point(250,300), greetingText) #Calls variable instead of putting text here
    greeting.setTextColor(color_rgb(0,0,0))
    greeting.setSize(15)
    greeting.setFace('arial')
    greeting.draw(win)

    #Little bit of fun 
    i=1
    while True== True:
        print(i)
        i += 1
        l=randint(1,4)
        x=randint(1,500)
        y=randint(1,400)
        if l==1:
            c='black'
        elif l==2:
            c='black'
        elif l==3:
            c='black'
        else:
            c='blue'
        win.plot(x, y, c)

    win.getMouse() #Pause before closing
main()


