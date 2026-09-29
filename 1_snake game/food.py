from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(0.4)
        self.color('red')
        self.shape('circle')
        self.appear()
    def appear(self):
        self.goto(random.randint(-250,250),random.randint(-250,250))