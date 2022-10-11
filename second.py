import turtle
from turtle import Screen,Turtle
import tkinter as tk

screen = Screen()
turtle.screensize(canvwidth=400, canvheight=300)
screen.title("Ehan's second project")
t = Turtle("turtle")
t.speed(-1)
turtle.bgcolor("cyan")
penSize = 1
colornames = ["red", "blue", "black", "white", "green", "yellow"]
indexcolor = 0
t.pencolor(colornames[indexcolor])

def dragging(x, y):
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)

def clickRight(x,y):
    t.clear()

def clickLeft(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def clickMiddle(x, y):
    global penSize
    penSize = 10
    t.pensize(penSize)


def onPlusPenSize():
    global penSize
    print("pen-size:", penSize)
    penSize += 1
    t.pensize(penSize)

def onMinusPenSize():
    global penSize
    print("pen-size:", penSize)
    penSize -= 1
    if penSize == 0:
        penSize = 1
        
    t.pensize(penSize)

def onNextColor():
    global colornames, indexcolor
    indexcolor += 1
    if indexcolor ==  len(colornames):
        indexcolor = 0
    t.pencolor(colornames[indexcolor])
    print(colornames[indexcolor])

def onSave():
    filename = "Turtle.eps"
    screen.getcanvas().postscript(file=filename)
    tk.messagebox.showinfo(title="save", message="Your drawing is saved in "+filename)

def addButtons():
    canvas = screen.getcanvas()
    btnPenPlus = tk.Button(canvas.master, text="+ pen-size", command=onPlusPenSize)
    btnPenMinus = tk.Button(canvas.master, text="- pen-size", command=onMinusPenSize)
    btnNextColor = tk.Button(canvas.master, text="Next color", command=onNextColor)
    btnSave = tk.Button(canvas.master, text="Save", command=onSave)
    canvas.create_window(-200, -350, window=btnPenPlus)
    canvas.create_window(-300, -350, window=btnPenMinus)
    canvas.create_window(+300, -350, window=btnNextColor)
    canvas.create_window(+400, -350, window=btnSave)
    
    

def main():
    turtle.listen()

    t.ondrag(dragging)
    turtle.onscreenclick(clickRight, 3)
    turtle.onscreenclick(clickLeft, 1)
    turtle.onscreenclick(clickMiddle, 2)

    # Add button
    addButtons()
    
    # infinite loop
    screen.mainloop()


main()
    
