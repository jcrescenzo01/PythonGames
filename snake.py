# program to copy the game snake, wherein a snake defined by blocks
# on a grid will eat snacks that appear, growing untill it dissapears by
# biting itself
# this will use OOP and will use the pygame module

# IMPORTS
import math
import random
import pygame       # needs to be installed
import tkinter as tk
from tkinter import messagebox

# CLASSES
class Cube(object):     # the cubes the snake eats
    rows = 0
    w = 0
    def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)):
        pass
    def move(self, dirnx, dirny):
        pass
    def draw(self, surface, eyes = False):
        pass

class Snake(object):        # the snake, which will contain cube objects
    def __init__(self):
        pass
    def move(self):
        pass
    def reset(self, pos):
        pass
    def addCube(self):
        pass
    def draw(self, surface):
        pass

# FUNCTIONS
def drawGrid(w, rows, surface):     # the grid
    # first figure out how big each square in the grid should be
    sizeBtwn = w // rows    # width integer divided by rows

    x=0
    y=0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn
        pygame.draw.line(surface, (255,255,255), (x,0),(x,w))
                        #window     color         startPosition,endPosition
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))
            # drawing 2 lines at every loop of the forloop
    pass

def redrawWindow(surface):  # fills screen with blakc, draws the grid, update display
    global rows, width
    win.fill((0, 0, 0))
    drawGrid(width, rows, surface)
    pygame.display.update()
    pass
def randomSnack(rows, items):
    pass
def message_box(subject, content):
    pass

# MAIN
def main():
    global width, rows
    width = 500     # width of the window
    #height = 500    # height of the window, unnecc because its gonna be a square anyway
    rows = 20       # rows in the grid that the snake will move on
    win = pygame.display.set_mode((width, height))    # creating the window
    s = snake((255,0,0), (10,10))   # color, position
    flag = True
    clock = pygame.time.Clock()     # a clock
    while flag:
        pygame.time.delay(50)   # delay 50ms every time so program doesnt run too fast
        clock.tick(10)      # uses clock to make sure game isnt more than 10fps
        redrawWindow(win)   # calls redrawWindow with win as the surface
    pass

"""
rows =
w =
h =

cube.rows = rows
cube.w = w

main()
"""


