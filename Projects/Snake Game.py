import turtle  # pip install PythonTurtle
import time
import random

# Step 1: default values for the game
delay = 0.1
score = 0
high_score = 0

# Step 2 : creating the display of the game, i.e, the window screen for the game where we will create the head of
# the snake and food for the snake in the game and displaying the scores at the header of the game.

# Creating a window screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("blue")
screen.setup(width=600, height=600)
screen.tracer(0)  # Turns turtle animation on/off and set delay for update drawings.

# head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()  # Pull the pen up -- no drawing when moving.
head.goto(0, 0)  # Move turtle to an absolute position.
head.direction = "Stop"

# food in the game
food = turtle.Turtle()
colors = random.choice(['red', 'green', 'black'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: 0, High Score: 0", align="center", font=("candara", 24, "bold"))


# Step 3: Now, validating the key for the snake’s movements. By clicking the keywords normally used for gaming
# ‘w’, ‘a’, ‘s’ and ‘d’, we can operate the snake’s movements around the screen.

# assigning key directions
def goup():
    if head.direction != "down":
        head.direction = "up"


def godown():
    if head.direction != "up":
        head.direction = "down"


def goleft():
    if head.direction != "right":
        head.direction = "left"


def goright():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.sety(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.sety(x + 20)


screen.listen()
screen.onkeypress(goup, "w")
screen.onkeypress(godown, "s")
screen.onkeypress(goleft, "a")
screen.onkeypress(goright, "d")

# Step 4: Now, we will create the gameplay

segments = []

# Main Gameplay
while True:
    screen.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        colors = random.choice(['red', 'green', 'black'])
        shapes = random.choice(['square', 'triangle', 'circle'])
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))

    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")  # tail colour
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))

    # Checking for head collisions with body segments
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"
            colors = random.choice(['red', 'green', 'black'])
            shapes = random.choice(['square', 'triangle', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segment.clear()

            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(score, high_score), align="center",
                      font=("candara", 24, "bold"))

    time.sleep(delay)

screen.mainloop()
