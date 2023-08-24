import tkinter as tk
from turtle import TurtleScreen,RawTurtle
import turtle

def draw_square():
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
def penup():
    turtle.penup()
def draw_outline():
    turtle.forward(660)
    turtle.right(90)
    turtle.forward(660)
    turtle.right(90)
    turtle.forward(660)
    turtle.right(90)
    turtle.forward(660)

root = tk.Tk('2000*2000')
canvas=tk.Canvas(root,width=900,height=600)
canvas.pack()
screen=TurtleScreen(canvas)
turtle=RawTurtle(screen)
button=tk.Button(root,text="Draw rooms of plan",comman=draw_square)
button1=tk.Button(root,text="draw outline of the plan",comman=draw_outline)
button2=tk.Button(root,text="to change the drawer",comman=penup)
button.pack()
root.mainloop()
turtle.penup()
turtle.forward(30)




