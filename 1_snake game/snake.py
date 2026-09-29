from turtle import Turtle
from time import sleep
class Snake():
    def __init__(self):
        self.parts = []
        self.place = -15
        self.creat()
    def creat(self):
        for _ in range(3):
            new_part = Turtle("square")
            new_part.shapesize(0.75)
            new_part.color('white',"gray")
            new_part.penup()
            new_part.goto(self.place,0)
            self.place += 15
            self.parts.append(new_part)
        self.head = self.parts[-1]
        self.head.shape('triangle')
        
    def move(self):
        for i in range(len(self.parts)-1):
            self.parts[i].goto(self.parts[i+1].pos())
        self.head.forward(15)

    def tall(self):
            new_part = Turtle("square")
            new_part.color('white',"gray")
            new_part.shapesize(0.75)
            new_part.penup()
            self.parts.insert(0,new_part)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self): 
        if self.head.heading() != 90:
            self.head.setheading(270)
 

