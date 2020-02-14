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
    #sum of squares (doesn't really change the heuristic)
    distance = (((len(maze)-1) - i)**2) + (((len(maze[0])-1) - j)**2)
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
