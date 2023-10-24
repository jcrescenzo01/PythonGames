# Simple Pon in Python 3 for Beginners
# Start
# we are using oldschool programming, no OOP and that kind of stuff, just to introduce games

# IMPORTS
import turtle       # module for Graphics, built in unlike pygame
import time         # to stop the program after 5 seconds on the win screen
import os           # linux and mac sound application
import winsound     # windows sound application

# Screen itself
wn = turtle.Screen()    # a window
wn.title("Pong by JC")      # window title
wn.bgcolor("black")     # sets the background color of the window
wn.setup(width=800, height=600)     # height and width of the window set
wn.tracer(0)    # stops the window from updating, so it must be manually updated
                # speeds up the game quite a lot

# Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()  # a turtle object called paddle_a representing the left paddle
paddle_a.speed(0)   # sets the speed of the ANIMATION of the paddle, not the literal movement
                    # sets it to the max possible speed
paddle_a.shape("square")    # sets the shape of the paddle to that of a square, (20px X 20px)
paddle_a.color("green")     # made the paddle green
paddle_a.shapesize(stretch_wid=5,stretch_len=1)     # changes the size of a shape by 20s, 5x20=100px, 1 is the default (?)
paddle_a.penup()    # stops it from "drawing while moving" which is something Turtles do by default
                    # assumedly like stopping it from holding down the draw button in paint!
paddle_a.goto(-350,0)   # puts the paddle where it starts at, so -350 is near the left of the screen
                        # and 0 is near the middle by height, -350W,0H

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("green")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350,0)   # +350 so its on the right side of the screen

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("green")
ball.penup()
ball.goto(0,0)
# we now need to seperate the balls movement into two parts, x and y movement
#ball.dx = 2     # every time our ball moves, it moves by 2 pixels for x
#ball.dy = 2     # for y. After this we go into the main game loop
    # the tutorial did 2, but thats very fast for me seemingly:
ball.dx = 1
ball.dy = 1


# Pen (a Turtle object) for Score System
pen = turtle.Turtle()
pen.speed(0)    # animation, not movement
pen.color("green")
pen.penup()
pen.hideturtle()    # hides it, we want to see the text it writes not the pen itself
pen.goto(0, 260)    # score will be around the top of the screen but not all the way
pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


# Function: move paddle a and b up and down
# for paddle a:
def paddle_a_up():
    y = paddle_a.ycor()     # we need to know the current y coordinate first
                            # .ycor() returns the y coordinate of a turtle obj
    y += 20   # adds 20px to the y coordinate
    paddle_a.sety(y)    # sets y to the current y
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

# for paddle b:
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard Binding
wn.listen()     # tells it to listen for keyboard input
wn.onkeypress(paddle_a_up, "w")   # when the user presses "w", call the funct paddle_a_up()
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")    # "Up" refers to the up arrow key
wn.onkeypress(paddle_b_down, "Down")    # "Down" for down arrow key


# Main Game Loop
while True:
    wn.update()     # Everytime the loop runs, it will update the screen
        # Ran it:
        # In a window, 0x0 is the center of the window, going neg or pos in distance depending on direction
        # this window is: 800w 600h, 0 is center so +300 and -300 Height, +400 and -400 Width

    # move the ball
    ball.setx(ball.xcor() + ball.dx)  # take the current x coord and add
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking - what happens when the ball hits the border?

    # Top Border; the height of the window is 600, so +300 is the top, but the ball is 20x20
    if ball.ycor() > 290:   # if the ball gets to a coord greater than 290px
        ball.sety(290)      # then set y to 290 so shit doesnt go wrong
        ball.dy *= -1   # reverses the direction, since negative would be the other way!
        # Audio
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)    # ASYNC means asyncronous, itll do it in the background, same as ampersand on mac and linux
        #MAC Sound
        #os.system("afplay bounce.wav") # just doing this alone will actually pause the sys when the sound plays
        #os.system("afplay bounce.wav&") # the ampersand (&) will fix this, though it delays due to the sound we're using being a bit lagged
            # afplay on mac, aplay on linux, and on windows its actually very different
                # import winsound, instead of os.system type winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    # Bottem Border
    if ball.ycor() < -290:  # to test this one, we have to go to dy and change it to negative so it goes the other direction!
        ball.sety(-290)
        ball.dy *= -1
        # Audio
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Right Border
    if ball.xcor() > 390:
        ball.goto(0,0)  # respawns the ball at 0,0
        #ball.setx(390)     # this works, but it isnt how pong works!, the ball getting past should make it dissapear!
        ball.dx *= -1
        score_a += 1
        pen.clear()  # clears the former pen, which said {0}{0}, so we can replace it with the updated numbers
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    # Left Border
    if ball.xcor() < -390:
        ball.goto(0,0)
        #ball.setx(-390)    # again, not what pong is a bout! this would bounce it
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
            # pen.write here is meant to increment the score by formatin it for screen updates
    # Paddle/Ball Collision Checking
    """
    if ball.xcor() > 340 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        # if the balls x coord is greater than 340, where the paddle would touch it, and is it between the top and bottem of the paddle
        ball.dx *= -1
        # with just this, the ball can get stuck behind the paddle and bounce off the wall due to
        # ,despite it being behind, the x coord is greater than 340 and is between the paddle and wall
    """
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        # added "and ball.xcor() < 350"
        ball.setx(340)  # moves it back left a bit
        ball.dx *= -1
        # Audio
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        # added "and ball.xcor() < 350"
        ball.setx(-340)  # moves it back right a bit
        ball.dx *= -1
        # Audio
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Ending the Game at Score 10 for a or b
    if score_a >= 10:
        pen.clear()
        pen.write("Player A Wins!".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        time.sleep(5)   # waits 5 seconds and pauses the game
        break       # ends the program
    elif score_b >= 10:
        pen.clear()
        pen.write("Player B Wins!".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        time.sleep(5)
        break

# POST GAME BUILD
# Adding sound! First download a sound file, .wav preferably (?)
# generally python is crossplatform, but sound screws with it, its a bit different between OS's
# wav files have good crossplatform compatability though
# placed sound file into same directory, we want it to play sound when the ball touches borders/paddles
# MAC and LINUX
    # now we "import os"
    # at border top and bottem, and paddle a and b:
        # os.system("afplay bounce.wav&")
            # afplay is apples music playing thing, & means async so it doesnt interrupt the program to play the sound
# WINDOWS
    # import winsound
    # at border top and bottem, and paddle a and b:
        # winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
            # winsound.PlaySound is windows method of playing sound, SND_ASYNC means send asyncroniously, ie dont interrupt/pause to play the sound