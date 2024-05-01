import turtle
import time 

# Set up screen
screen = turtle.Screen()
screen.title("Air Hockey")
screen.bgcolor("black")
screen.setup(width=700, height=500)

# Ball
ball = turtle.Turtle()
ball.speed(200)  # Adjust the speed of the ball
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 5  # Increase the speed of the ball in the x-direction
ball.dy = 5  # Increase the speed of the ball in the y-direction

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # Make the paddle vertical
paddle_a.penup()
paddle_a.goto(-340, 0)
paddle_a_speed = 30  # Adjust the speed of paddle A

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # Make the paddle vertical
paddle_b.penup()
paddle_b.goto(330, 0)
paddle_b_speed = 30  # Adjust the speed of paddle B

# Scores
score_a = 0
score_b = 0

# Score display turtle
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 160)

# Move paddle A up and down
def paddle_a_up():
    y = paddle_a.ycor()
    y += paddle_a_speed
    if y + 50 < 265:  # Check if the y-coordinate is within the screen limits
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= paddle_a_speed
    if y - 50 > -265:  # Check if the y-coordinate is within the screen limits
        paddle_a.sety(y)

# Move paddle B up and down
def paddle_b_up():
    y = paddle_b.ycor()
    y += paddle_b_speed
    if y + 50 < 265:  # Check if the y-coordinate is within the screen limits
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= paddle_b_speed
    if y - 50 > -265:  # Check if the y-coordinate is within the screen limits
        paddle_b.sety(y)

# Keyboard bindings
screen.listen()
screen.onkeypress(paddle_a_up, "w")
screen.onkeypress(paddle_a_down, "s")
screen.onkeypress(paddle_b_up, "Up")
screen.onkeypress(paddle_b_down, "Down")

# Delay the start of the game by 1 second
time.sleep(1)

    # Main game loop
while True:
    screen.update()

        
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # Border checking for the ball
    if ball.ycor() > 190 or ball.ycor() < -190:
        ball.dy *= -1

    # Paddle and ball collisions
    if (ball.xcor() > 290 and ball.xcor() < 300) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(290)
        ball.dx *= -1

    elif (ball.xcor() < -290 and ball.xcor() > -300) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-290)
        ball.dx *= -1

    # Scoring
    if ball.xcor() > 300:
        score_a += 1
        if score_a == 3:
            score_display.clear()
            score_display.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
            time.sleep(2)
            break
             
           

        else:
            ball.goto(0, 0)
            ball.dx *= -1
            score_display.clear()
            score_display.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
            time.sleep(1)  

    elif ball.xcor() < -300:
        score_b += 1
        if score_b == 3:
            score_display.clear()
            score_display.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
            time.sleep(3) # Keep the window open to show final score for 3 seconds
            break
              
                

        else:
            ball.goto(0, 0)
            ball.dx *= -1
            score_display.clear()
            score_display.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
            time.sleep(1)  

        turtle.update()