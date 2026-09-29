from turtle import Turtle 
class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.new_best = False
        self.goto(0,320)
        with open('1_snake game/best.txt') as np:
            self.best = int(np.read())
        self.score = 0
        self.write_score()
    def write_score(self):
        self.goto(0,320)
        self.write(self.score,font=('',20,''))
        self.goto(0,310)
        self.write(f'best: {self.best}',font=('',10,''))
    def update_score(self):
        self.clear()
        self.score += 1
        self.write_score()
    def game_over(self):
        if self.score > self.best:
            with open('snake game/best.txt','w+') as zp:
                zp.write(str(self.score))
            with open('snake game/best.txt')as zp:
                self.best = int(zp.read())
            self.new_best =True

        self.goto(0,0)
        self.write('****game over****',align='center',font=('',28,''))
        self.goto(0,-20)
        self.write(f'score: {self.score}',align='center',font=['',15,''])
        self.goto(0,-40)
        if self.new_best:
            self.write(f'new best score🥇: {self.best}',align='center',font=['',18,''])
        else:
            self.write(f'best: {self.best}',align='center',font=['',15,''])