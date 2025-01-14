from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('hungry snake')
screen.tracer(0)

snake=Snake()

current_direction='right'
game_on=True
def wrapper_up():
    global current_direction #for globally modify it
    if snake.up(current_direction):
        current_direction='up'
def wrapper_down():
    global current_direction #for globally modify it
    if snake.down(current_direction):
        current_direction='down'
def wrapper_left():
    global current_direction #for globally modify it
    if snake.left(current_direction):
        current_direction='left'
def wrapper_right():
    global current_direction #for globally modify 
    
    it
    if snake.right(current_direction):
        current_direction='right'
#for controlling the snake
screen.listen()
screen.onkey(wrapper_up,'Up')
screen.onkey(wrapper_down,'Down')
screen.onkey(wrapper_left,'Left')
screen.onkey(wrapper_right,'Right')
food=Food()
food.give_food(snake)

score=Score()

while game_on:
    #move the snake
    screen.update()
    time.sleep(0.12)
    snake.move()
    
    #collision with food
    if snake.head.distance(food)<20:
        score.score+=1
        score.update_score()
        snake.increase()
        food.give_food(snake)
    
    game_on=snake.dead()
    
score.over()
        

screen.exitonclick()

