from turtle import Screen
from time import sleep
from random import choice

from man import Man
from word import Word

wall = Screen()
wall.setup(600,600)
wall.bgcolor('cyan')

man = Man()
hunging =[    
man.man10,        
man.man9,
man.man8,
man.man7,
man.man6,
man.man5,
man.man4,
man.man3,
man.man2,
man.man1]

writer = Word()

man.make_area()

word = choice(('cat','soup','apple'))
gussed_word = ['_'] * len(word)
used_letters = []

trys = 10
game_on = True
is_win = False

letter = 'guss a letter'
while game_on:
    if ''.join(gussed_word) == word:
        is_win = True
        game_on = False
    else:
        writer.write_word(gussed_word)
        gussed_letter = wall.textinput(f'trys:{trys}',letter).lower()
        if gussed_letter in used_letters:
            letter = 'you tryed that before'
        else:
            if gussed_letter not in used_letters:
                if gussed_letter in word:
                    for i in range(len(word)):
                        if word[i] == gussed_letter:
                            gussed_word[i] = gussed_letter
                    letter = 'corecct guss another letter'
                else:
                    letter = 'wrong try to guss again'
                    trys = trys - 1
                    used_letters.append(gussed_letter)
                    hunging[trys]()
    if gussed_letter not in used_letters:
        used_letters.append(gussed_letter)
    if trys <= 0:
        game_on = False
    sleep(1)
writer.write_word(gussed_word)
writer.goto(0,0)
if is_win:
    wall.bgcolor('green')
    massage = 'you win'
else:
    wall.bgcolor('red')
    massage = 'you lose'
writer.write(massage,align='center',font=('',30,''))
    



wall.mainloop()
#wall.exitonclick()