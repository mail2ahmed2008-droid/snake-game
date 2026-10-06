from turtle import Turtle
class Word(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0,250)
    def write_word(self,word=list,spase=' '):
        self.clear()
        self.write(spase.join(word),align= 'center' ,font=('',30,''))