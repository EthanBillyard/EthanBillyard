
#Sketchbook / Drawing Application
from tkinter import *
sketchbook = Tk()
sketchbook.title("Sketchbook")

#Variables
bgColour = "White"
sidePanelBGColour = "#EEEEEE"
colour = "black"
penSize = 2
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500

#Main window
sketchbook.geometry("800x500+400+200")

#Create a canvas
canvas = Canvas(sketchbook, bg = bgColour, width = 0.8 * WINDOW_WIDTH, height = 0.98 * WINDOW_HEIGHT)
canvas.grid(row = 0, column = 0, sticky = "n", padx = 1, pady = 1)

#Side Panel
sidePanel = Frame(sketchbook, width = 0.18 * WINDOW_WIDTH, height = 500, bg = sidePanelBGColour)
sidePanel.grid(row = 0, column = 1, sticky = "n", padx = 1, pady = 1)

#Allows pen colours to be changed
def setColour(newcolour):
    global colour
    colour = newcolour

#Creates Buttons for pen colour selection
colourSelection=["black", "red", "green", "blue", "cyan", "yellow", "magenta","white"]
counter=10
def colourLambda(var):
	return lambda x: setColour(var)
#Creates a box for each colour
#If mouse click on box then trigger colour change
def colourBoxes():
    for current in colourSelection:
        global counter
        id = canvas.create_rectangle((10, counter, 30, counter+20), fill=current)
        canvas.tag_bind(id, "<Button-1>", colourLambda(current))
        counter = counter + 25

colourBoxes()

#Changes Pen Size
def setPenSize(newPenSize):
    global penSize
    penSize = newPenSize

penSizeLabel = Label(sidePanel, text = "Pen Size")
penSizeLabel.grid(row = 4, column = 0)

penSizeEntry = Entry(sidePanel, textvariable = str(setPenSize), justify = "center", width = 4)
penSizeEntry.grid(row = 5, column = 0)

penSizeButton = Button(sidePanel, text = "Change Pen Size", command = lambda: setPenSize(penSizeEntry.get()), justify = "center")
penSizeButton.grid(row = 6, column= 0, pady = 5)

#Explains how to use the program
tutorial = Label(sidePanel, text = "\nHow to Use: \n Click on the white box\nwith a mouse or tablet\nto draw. Click on a\ncoloured box on the\nleft if you wish to\nchange colours. Click the\n'reset canvas' button\nbelow to start over.\n")
tutorial.grid(row = 7, column = 0)

#Reset Canvas
def clearCanvas():
    counter = 10
    canvas.delete("all")
    colourBoxes()

clearCanvasButton = Button(sidePanel, text = "Clear Canvas", command = clearCanvas, justify = "center")
clearCanvasButton.grid(row = 8, column = 0)

#Draw using a mouse or tablet by clicking and dragging on canvas
    #Stores coordinates of mouse click
def getXAndYCoordinates(event):
    global lastX, lastY
    lastX = event.x
    lastY = event.y

    #Puts an oval where mouse was clicked
def draw(event):  
    global lastX, lastY, colour, penSize
    canvas.create_oval((lastX, lastY, event.x, event.y), fill = colour, outline = colour, width = penSize)
    lastX = event.x
    lastY = event.y

    #Draw on canvas by storing coordinate and making an oval every time the mouse moves, emulates the way a physical pen works
canvas.bind("<Button-1>", getXAndYCoordinates)
canvas.bind("<B1-Motion>", draw)

sketchbook.mainloop()