from tkinter import *
import random

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
    window.bind()

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
x = (width - window.winfo_reqwidth()) // 2
y = (height - window.winfo_reqheight()) // 2

window.mainloop()