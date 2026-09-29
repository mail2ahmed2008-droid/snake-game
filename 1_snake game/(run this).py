from turtle import Screen,Turtle
from time import sleep

from score import Board
from snake import Snake
from food import Food

screen = Screen()
screen.setup(700,700)
screen.bgcolor("black")
screen.tracer(0)
t=Turtle()
# creat earea
t.penup()
t.goto(300,300)
t.pendown()
t.setheading(180)
t.pensize(10)
t.color('blue')
for _ in range(4):
    t.forward(600)
    t.left(90)
t.hideturtle()
# earea has done
snake = Snake()
apple = Food()
score = Board()

screen.listen()
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
game_on = True
screen.update()
while game_on:
    # if the snake eat it self
    for i in snake.parts:
        if i.distance(snake.head) == 0 and i != snake.head:
            game_on = False
            break
    if snake.head.distance(apple) < 15:
        apple.appear()
        score.update_score()
        snake.tall()
    # if the snake hit the wall
    if (snake.head.xcor() > 260 or 
        snake.head.xcor() < -260 or
        snake.head.ycor() > 260 or
        snake.head.ycor() < -260):
        game_on = False

    snake.move()
    screen.update()
    sleep(0.1)
screen.bgcolor('red')
sleep(1)
for i in snake.parts[::-1]:
    i.hideturtle()
    screen.update()
    sleep(0.1)
score.game_over()
screen.update()
screen.exitonclick()