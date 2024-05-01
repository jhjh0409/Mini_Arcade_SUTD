#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import libraries
import turtle
import time
import random

delay = 0.1
log_speed = 5

# Set up the screen
win = turtle.Screen()
win.title("lumberjack")
win.bgcolor("yellow")
win.setup(width=600, height=600)
win.tracer(0)

# Creating the Lumberjack 
lumberjack = turtle.Turtle()
lumberjack.speed(0)
lumberjack.shape("square")
lumberjack.color("darkblue")
lumberjack.shapesize(stretch_wid=1, stretch_len=2)
lumberjack.penup()
lumberjack.goto(0, -250)

# Logs
logs = []

# Score
score = 0

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

# Game over display
game_over_display = turtle.Turtle()
game_over_display.speed(0)
game_over_display.color("red")
game_over_display.penup()
game_over_display.hideturtle()
game_over_display.goto(0, 0)

# Creating the falling logs
def create_log():
    log = turtle.Turtle()
    log.speed(0)
    log.shape("square")
    log.color("brown")
    log.shapesize(stretch_wid=1, stretch_len=random.uniform(1, 2))
    log.penup()
    x = random.randint(-290, 290)
    y = random.randint(100, 250)
    log.goto(x, y)
    logs.append(log)

for _ in range(6):
    create_log()

# Functions
def move_left():
    x = lumberjack.xcor()
    if x > -280:
        lumberjack.setx(x - 20)

def move_right():
    x = lumberjack.xcor()
    if x < 280:
        lumberjack.setx(x + 20)

def game_over():
    global score
    game_over_display.clear()
    game_over_display.write("Game Over", align="center", font=("Courier", 36, "normal"))
    time.sleep(2)
    game_over_display.clear()
    score = 0
    reset_game()

def reset_game():
    global log_speed
    lumberjack.goto(0, -250)
    for log in logs:
        x = random.randint(-290, 290)
        y = random.randint(100, 250)
        log.goto(x, y)
        log.shapesize(stretch_wid=1, stretch_len=random.uniform(1, 2))
    # Reset log speed
    log_speed = 5 
    score_display.clear()
    score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

# Keyboard bindings
win.listen()
win.onkey(move_left, "Left")
win.onkey(move_right, "Right")

# Main game loop
while True:
    win.update()

    # Move the logs
    for log in logs:
        y = log.ycor()
        x = log.xcor()
        log.sety(y - log_speed)
        log.setx(x + random.uniform(-20, 20))  # Random horizontal movement

        # Check for collision with the lumberjack
        if lumberjack.distance(log) < 20:
            game_over()

        # Check for logs reaching the bottom
        if log.ycor() < -290:
            y = random.randint(100, 250)
            x = random.randint(-290, 290)
            log.goto(x, y)
            log.shapesize(stretch_wid=1, stretch_len=random.uniform(1, 2))
            score += 1
            score_display.clear()
            score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

        # Check for scoring
        if log.ycor() < lumberjack.ycor() < log.ycor() + 20 and log.xcor() - 20 < lumberjack.xcor() < log.xcor() + 20:
            score += 1
            score_display.clear()
            score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    # Increase log speed over time
    log_speed += 0.1

    time.sleep(delay)


# In[ ]:





# In[ ]:




