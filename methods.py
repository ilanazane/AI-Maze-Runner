#Some imports
import numpy as np
import matplotlib.pyplot as plt
import random
import queue
import time

#Functions that will be very useful for creating/updating mazes

'''
Define the grid to be working with
            **inputs**
-dim = dimension size of the grid
-p = probability that a grid spot will be filled or open
            **returns**
-maze = the grid to be worked with
'''


def grid(dim, p):
    #start with a dim by dim zero array
    maze = np.zeros((dim,dim))
    for item in range(dim):
        for thing in range(dim):
            #makes sure the top left spot is empty
            if item == 0 and thing == 0:
                pass
            #makes sure the bottom right spot is empty
            elif item == dim - 1 and thing == dim - 1:
                pass
            #change the cells based off of the value of p and our random number, x
            else:
                x = random.random()
                #if our random number is less than p, then the cell will not be filled
                if p < x:
                    maze[item][thing] = 0
                #if our random number is greater than p, then the cell will  be filled
                else:
                    maze[item][thing] = 1
    #return the grid to be worked with
    return maze


'''
update the state of the maze after moving to the next tile
            **inputs**
-maze = the maze to be updated
-i = which row to update
-j = which column to update
'''


def update(maze, i, j):
    #shades the tile grey to distinguish between open and occupied
    maze[i][j] = 0.5


'''
Euclidean Heuristic (taking the square root resulted in issues regarding rounding float values)
This was resolved by just using the sum of the squares (still gives same results)
            **inputs**
-maze = the maze being worked with
-i = the current row to use in calculation
-j = the current column to use in calculation
            **returns**
-distance = the Euclidean distance
'''


def Euclidean(maze, i, j):
    x = [len(maze) - 1, len(maze) - 1]
    y = [i, j]
    distance = np.sqrt( (y[0]-x[0])**2 + (y[1]-x[1])**2 )
    return distance


'''
Manhattan Heuristic
            **inputs**
-maze = the maze being worked with
-i = the current row to use in calculation
-j = the current column to use in calculation
            **returns**
-distance = the Manhattan distance
'''


def Manhattan(maze, i, j):
    distance = abs(len(maze)-1 - i) + abs(len(maze[0])-1 - j)
    return distance


'''
Create a grid to be worked on with an initial cell on fire
            **inputs**
-dim = the dimension size of the maze
-p = probability that a grid spot will be filled or open
            **returns**
-maze = the grid to be worked with
'''


def firegrid(dim, p):
    #start with a dim by dim zero array
    maze = np.zeros((dim,dim))
    for item in range(dim):
        for thing in range(dim):
            #makes sure the top left spot is empty
            if item == 0 and thing == 0:
                pass
            #makes sure the bottom right spot is empty
            elif item == dim - 1 and thing == dim - 1:
                pass
            #change the cells based off of the value of p and our random number
            else:
                x = random.random()
                #if our random number is less than p, then the cell will not be filled
                if p < x:
                    maze[item][thing] = 0
                #if our random number is greater than p, then the cell will  be filled
                else:
                    maze[item][thing] = 1
    #return the grid to be worked with

    r = random.randrange(0,dim-1,1)
    s = random.randrange(0,dim-1,1)
    if maze[r][s]==0:
        maze[r][s]=0.75
    else:
        while maze[r][s]==1:
            r = random.randrange(0,dim-1,1)
            s = random.randrange(0,dim-1,1)
        maze[r][s]=0.75

    return maze


'''
Count the number of neighbors on fire
            **inputs**
-maze = the maze being worked with
-i = the current row to use in calculation
-j = the current column to use in calculation
-dim = the dimension size of the maze being worked with
            **returns**
-k = the number of neighbors on fire
'''


def countFires(maze, i, j, dim):
    k=0
    if i!= dim-1 and maze[i+1][j]==0.75:
        k+=1
    if j!= dim-1 and maze[i][j+1]==0.75:
        k+=1
    if i!=0 and maze[i-1][j]==0.75:
        k+=1
    if j!=0 and maze[i][j-1]==0.75:
        k+=1
    return k


'''
Probabilistically update the fire state of every cell depending on the number of neighboring cells on fire
            **inputs**
-maze = the maze being worked with
-q = a number between 0 and 1, dictating the rate that the fire spreads
            **returns**
-maze = the updated maze
'''


def updateFire(maze, q, dim):
    for item in range(dim):
        for thing in range(dim):
            k = countFires(maze, item, thing, dim)
            #print(k)
            p = 1-((1-q)**k)
            x = random.random()
            if p > x and maze[item][thing]!=1:
                maze[item][thing] = 0.75
    return maze


'''
Fire heuristic that accounts for probability of a cell being on fire 
            **inputs**
-maze = the maze being worked with
-i = the current row to use in calculation
-j = the current column to use in calculation
-q = a number between 0 and 1, dictating the rate that the fire spreads
            **returns**
-distance = the Manhattan distance with added probability a neighboring cell is going to catch on fire
'''


def firemanhattan(maze, i, j, q):
    k = countFires(maze, i, j, len(maze))
    p = 1-((1-q)**k)
    distance = abs(len(maze)-1 - i) + abs(len(maze[0])-1 - j)+(len(maze)*p)
    return distance
