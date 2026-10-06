from turtle import Turtle
class Man(Turtle):
    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.hideturtle()
    def make_area(self):
        self.penup()
        self.begin_fill()
        self.goto(-1000,-200)
        self.pendown()
        self.begin_fill()
        for _ in range(2):
            self.forward(2000)
            self.right(90)
            self.forward(300)
            self.right(90)
        self.end_fill()

    def man1(self):
        self.penup()
        self.goto(-70,-200)
        self.color('yellow')
        self.pendown()
        self.begin_fill()
        for _ in range(2):
            self.forward(140)
            self.left(90)
            self.forward(50)
            self.left(90)
        self.end_fill()

    def man2(self):
        self.penup()
        self.color('brown')
        self.goto(50,-150)
        self.pendown()
        self.left(90)
        self.pensize(10)
        self.forward(200)

    def man3(self):
        self.left(90)
        self.forward(100)

    def man4(self):
        self.pensize(3)
        self.color('black')
        self.left(90)
        self.forward(50)

    def man5(self):
        self.right(90)
        self.circle(10)

    def man6(self):
        self.left(90)
        self.penup()
        self.forward(20)
        self.pendown()
        self.forward(50)
        self.left(180)
        self.forward(45)

    def man7(self):
        self.right(135)
        self.forward(30)
        self.left(180)
        self.forward(30)

    def man8(self):
        self.left(90)
        self.forward(30)
        self.left(180)
        self.forward(30)
    
    def man9(self):
        self.penup()
        self.goto(-50,-70)
        self.setheading(315)
        self.pendown()
        self.forward(30)
        self.left(180)
        self.forward(30)

    def man10(self):
        self.left(90)
        self.forward(30)
        
        