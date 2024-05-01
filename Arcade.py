import argparse
import turtle
import time
import random
import math
from tkinter import *

def game_menu():
    print("Welcome to the Game Menu!")
    print("Select a game:")
    print("1 - Snake")
    print("2 - Space Shooter")
    print("3 - Lumberjack")
    print("4 - Air Hockey")
    choice = input("Enter the number of the game you want to play: ")
    if choice.isdigit() and (0 < int(choice) < 5):
        return int(choice)

# Define functions for each game
def start_snake():

    # Defining Global Variables
    width, height = 600, 600
    speed = 70
    size = 30
    snake_body = 3
    snake_colour = "#50C878"
    food_colour = "#D22B2B"
    background_colour = "#000000"

    # Defining Objects - Snake & Apple
    class Snake():
        
        def __init__(self):
            self.body_size = snake_body
            self.coordinates = []
            self.squares = []

            # Creating initial position of snake
            for i in range(snake_body):
                self.coordinates.append([0,0])

            # Creating the graphics for the snake
            for x, y in self.coordinates:
                square = canvas.create_rectangle(x, y, x+size, y+size, fill=snake_colour)
                self.squares.append(square)

    class Apple():
        
        def __init__(self):
            # Generating random x and y coordinates
            x = random.randint(0, int((width/size)-1)) * size
            y = random.randint(0, int((height/size)-1)) * size

            # Setting initial coordinates of food
            self.coordinates = [x, y]

            # Creating food object
            canvas.create_oval(x, y, x+size, y+size, fill=food_colour, tag="apple")


    # Defining Functions
    def game_over():
        
        # Stop game
        canvas.delete(ALL)
        canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('helvetica', 50),  text="GAME OVER",  fill="red", tag="gameover")

        # Start new game
        canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/1.5, font=('helvetica', 30),  text="Double click to start new game",  
                        fill="green", tag="newgame")
        window.bind('<Double-Button-1>', start_game)
        label.after(1000, label.destroy())

    def run_game(*arg):

        canvas.delete(ALL)
        snake = Snake()
        apple = Apple()
        game_controls(snake, apple)

    def game_controls(snake, apple):
        
        # Get coordinates of head of snake
        x, y = snake.coordinates[0]

        # Check initial direction of snake and adjust the position of head
        if direction == "up":
            y -= size
        elif direction == "down":
            y += size
        elif direction == "left":
            x -= size
        elif direction == "right":
            x += size

        # Update the coordinates of head of snake
        snake.coordinates.insert(0, (x,y))

        # Update the graphics of the head of snake
        square = canvas.create_rectangle(x, y, x+size, y+size, fill=snake_colour)
        snake.squares.insert(0, square)

        # If the snake head is at apple, update the scoreboard and then create a new apple.
        if x == apple.coordinates[0] and y == apple.coordinates[1]:

            global score
            
            score += 1
            label.config(text=f"Score:{score}")
            canvas.delete("apple")

            apple = Apple()
            # If apple spawns in snake, delete the old apple and create a new one.
            for square in snake.coordinates[::]:
                if apple.coordinates[0] == square[0] and apple.coordinates[1] == square[1]:
                    canvas.delete("apple")
                    apple = Apple()
        
        else:
            # Update tail of snake
            del snake.coordinates[-1]
            canvas.delete(snake.squares[-1])
            del snake.squares[-1]

        if check_collisions(snake):
            # Show Game Over
            game_over()

        else:
            # Repeat function
            window.after(speed, game_controls, snake, apple)

    def movement(new_direction):
        
        global direction

        # Check if the new direction is opposite from current direction, preventing snake from reversing
        # If new direction is not opposite, change the direction of snake.
        if new_direction == 'left':
            if direction != 'right':
                direction = new_direction
        elif new_direction == 'right':
            if direction != 'left':
                direction = new_direction
        elif new_direction == 'up':
            if direction != 'down':
                direction = new_direction
        elif new_direction == 'down':
            if direction != 'up':
                direction = new_direction

    def check_collisions(snake):

        # Get coordinates of snake head
        x, y = snake.coordinates[0]

        # Check if head of snake is beyond the border
        if x < 0 or x >= width:
            return True
        elif y < 0 or y >= height:
            return True
        
        # Loop through the coordinates of the snake body, checking for collisions
        for square in snake.coordinates[1:]:
            if x == square[0] and y == square[1]:
                return True
            
        return False

    def main():
        global label, direction, score
        # Initializing initial score and direction
        score = 0
        direction = 'down'


        # Creating scoreboard label
        label = Label(window, text=f"Score: {score}", font=('helvetica', 20))
        label.pack(side=LEFT)

        # Binding keyboard buttons to movement controls
        window.bind('<Left>', lambda event: movement('left'))
        window.bind('<Key-a>', lambda event: movement('left'))
        window.bind('<Right>', lambda event: movement('right'))
        window.bind('<Key-d>', lambda event: movement('right'))
        window.bind('<Up>', lambda event: movement('up'))
        window.bind('<Key-w>', lambda event: movement('up'))
        window.bind('<Down>', lambda event: movement('down'))
        window.bind('<Key-s>', lambda event: movement('down'))
        window.bind('<Escape>', lambda event: window.destroy())

        run_game()


    # Creating Game Window
    window = Tk()
    window.title("SNAKE")
    window.resizable(False, False)


    # Creating Game Canvas
    canvas = Canvas(window, bg=background_colour, height=height, width=width)
    canvas.pack()


    def start_game(*arg):
        start_button.destroy()
        main()

    start_button = Button(window, text="Start Game", command=start_game, width=15, height=2, font=("Arial", 16))
    start_button.place(relx=0.5, rely=0.5, anchor=CENTER)

    window.mainloop()

def start_space_shooter():
    #Set up initial screen
    wn = turtle.Screen()
    wn.setup(width=600, height=600)
    wn.title("Space Shooter Game")
    wn.bgcolor('black')
    turtle.color('white')
    turtle.write("< SPACE SHOOTER GAME > \nPress R to start \nLeft Key - Turn Left \nRight Key - Turn Right \nSpace Bar - Shoot",False,align = "center", font = ("Courier", 24, "normal"))
    turtle.hideturtle()
    # Stop screen updates
    wn.tracer(0)

    # Create Shooter shape
    shooter_vertices = ((0,15),(-15,0),(-18,5),(-18,-5),(0,0),(18,-5),(18, 5),(15, 0))
    wn.register_shape("player",shooter_vertices)

    #Create asteroid shape
    asteroid_vertices = ((0, 10), (5, 7), (3,3), (10,0), (7, 4), (8, -6), (0, -10), (-5, -5), (-7, -7), (-10, 0), (-5, 4), (-1, 8))
    wn.register_shape("asteroid",asteroid_vertices)


    #Create class 'Sprite'
    class Sprite(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            # Maximum animation speed
            self.speed(0)
            self.penup()

    #Create Function to deter
    def get_heading_to(t1, t2):
        x1 = t1.xcor()
        y1 = t1.ycor()
        
        x2 = t2.xcor()
        y2 = t2.ycor()
        
        heading = math.atan2(y1 - y2, x1 - x2)
        heading = heading * 180.0 / math.pi
        
        return heading

    #Create variable for shooter and scoreboard
    player = Sprite()
    player.color("lightslateblue")
    player.shape("player")
    pen = Sprite()
    pen.color("white")

    # Set missile
    missiles = []
    for _ in range(3):
        missile = Sprite()
        missile.color("lawngreen")
        missile.shape("square")
        missile.shapesize(stretch_wid = 0.3,stretch_len=0.7)
        missile.speed = 1
        missile.state = "ready"
        missile.hideturtle()
        missiles.append(missile)

    #Create function for resetting of scoreboard
    def set_scoreboard(pen):
        pen.goto(0, 250)
        pen.write("Score: 0", False, align = "center", font = ("Courier", 24, "normal"))
        pen.hideturtle()

    #Create function for resetting of asteroid
    def set_asteroids(asteroids):
        for _ in range(5):   
            asteroid = Sprite()
            asteroid.color("Darkkhaki")
            asteroid.shape("asteroid")
            asteroid.speed = random.randint(3,6)/100
            asteroid.goto(0, 0)
            heading = random.randint(0, 260)
            distance = random.randint(300, 400)
            asteroid.setheading(heading)
            asteroid.fd(distance)
            asteroid.setheading(get_heading_to(player, asteroid))
            asteroids.append(asteroid)
            #asteroid.speed += 0.001


    # Create functions for different commands    
    def rotate_left():
        player.lt(15)
        
    def rotate_right():
        player.rt(15)
        
    def fire_missile():
        for missile in missiles:
            if missile.state == "ready":
                missile.goto(0, 0)
                missile.showturtle()
                missile.setheading(player.heading())
                missile.state = "fire"
                break

    #Main Game function
    def start_game():
        #Reset Game
        turtle.hideturtle()
        turtle.clear()
        asteroids = []
        pen.clear()
        wn.setup(width=600, height=600)
        wn.bgcolor('black')
        wn.tracer(0)
        player.score = 0
        player.goto(0, 0)
        player.showturtle()
        set_scoreboard(pen)
        set_asteroids(asteroids)
        Game_Over = False
        count = 0
        #Main game loop
        while Game_Over == False:
            # Do screen update
            wn.update()
            # Set keys for respective commands
            wn.listen()
            wn.onkey(rotate_left, "Left")
            wn.onkey(rotate_right, "Right")
            wn.onkey(fire_missile, "space")
        
            # Move the missile
            for missile in missiles:
                if missile.state == "fire":
                    missile.fd(missile.speed)
            
                # Check for borders
                if missile.xcor() > 300 or missile.xcor() < -300 or missile.ycor() > 300 or missile.ycor() < -300:
                    missile.hideturtle()
                    missile.state = "ready"

            # Iterate through asteroids
            for asteroid in asteroids:    
                # Move the asteroid
                asteroid.fd(asteroid.speed)

            
            # Check for collisions
                # Asteroid and Player
                if asteroid.distance(player) < 20:
                    # Reset Asteroid
                    heading = random.randint(0, 260)
                    distance = random.randint(600, 800)
                    asteroid.setheading(heading)
                    asteroid.fd(distance)
                    asteroid.setheading(get_heading_to(player, asteroid))
                    Game_Over = True
                    pen.clear()
                    pen.write("Score: {}".format(player.score), False, align = "center", font = ("Courier", 24, "normal"))
                    
                # Asteroid and Missile
                for missile in missiles:
                    if asteroid.distance(missile) < 20:
                        # Reset Asteroid
                        heading = random.randint(0, 260)
                        distance = random.randint(600, 800)
                        asteroid.setheading(heading)
                        asteroid.fd(distance)
                        asteroid.setheading(get_heading_to(player, asteroid))
                        
                        
                        # Reset Missile
                        missile.goto(600, 600)
                        missile.hideturtle()
                        missile.state = "ready"
                        
                        # Increase score
                        player.score += 10
                        count +=1
                        pen.clear()
                        pen.write("Score: {}".format(player.score), False, align = "center", font = ("Courier", 24, "normal"))


            #Set Game Over screen    
            if Game_Over == True:
                player.hideturtle()
                missile.hideturtle()
                for a in asteroids:
                    a.hideturtle()
                pen.clear()
                #wn.clear()
                wn.bgcolor('black')
                pen.write("Press R to restart",False,align = "center", font = ("Courier", 24, "normal"))
                turtle.color('firebrick1')
                turtle.write('GAME OVER!',False,align = "center", font = ("Courier", 50, "bold"))
                break
                
                
    #Set command to restart Game            
    wn.listen()
    wn.onkey(start_game,'r')

    wn.mainloop()

def start_lumberjack():

    global log_speed, score
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
    def game_loop():
        global log_speed, score
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

        win.ontimer(game_loop, int(delay * 1000))

    # Start the game loop
    game_loop()

    # Start the main loop
    turtle.mainloop()

def start_air_hockey():
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

# Parse command line arguments to select the game
def parse_arguments():
    parser = argparse.ArgumentParser(description="Arcade Game Selection")
    parser.add_argument("-g", "--game", type=int, choices=[1, 2, 3, 4], help="Select a game: 1 - Snake, 2 - Space Shooter, 3 - Lumberjack, 4 - Air Hockey")
    return parser.parse_args()

if __name__ == "__main__":
    #args = parse_arguments()

    # Run the selected game based on user input
    choice = game_menu()
    if choice == 1:
        start_snake()
    elif choice == 2:
        start_space_shooter()
    elif choice == 3:
        start_lumberjack()
    elif choice == 4:
        start_air_hockey()
    else:
        print("Invalid game selection. Please choose a game by entering a number between 1 and 4.")