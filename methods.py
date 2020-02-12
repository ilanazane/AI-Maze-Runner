import numpy as np
import matplotlib.pyplot as plt
import random
import queue
import time
from IPython.display import clear_output

#Functions that will be very useful for creating/updating mazes

'''
Define the grid to be working with

            **inputs**

-dim = dimension size of the grid 
-p = probability that a grid spot will be filled or open

            **returns**
            
-a = the grid to be worked with
'''

def grid(dim, p):
    #start with a dim by dim zero array
    a = np.zeros((dim,dim))
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
                    a[item][thing] = 0
                #if our random number is greater than p, then the cell will  be filled
                else:
                    a[item][thing] = 1
    #return the grid to be worked with
    return a


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
Euclidean Heuristic 

            **inputs**

-maze = the maze being worked with
-i = the current row to use in calculation
-j = the current column to use in calculation

            **returns**
            
-distance = the Euclidean distance
'''
    
def Euclidean(maze, i, j):
    distance = np.sqrt(pow(len(maze)-1 - i, 2) + pow(len(maze[0])-1 - j, 2))
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
Random Walk Function to make 'hard' mazes

            **inputs**

-maze = the maze being worked with
-times_changed = the number of times the maze has been updated (usually 0 to start)

            **returns**
            
-maze = the updated maze
'''

def randomWalk(maze,times_changed):
    print(times_changed)
    if times_changed > 4:
        return maze
    else:
        mazeOriginal=np.copy(maze)
        maze2 = np.copy(maze)
        #call BFS with original maze
        x=BFS(maze2,video=False)
        pathLength1=x[1]
        #if BFS is solvable
        if x[0]==1:
            y=random.random()
            #add obstacle
            if y > 0:
                while True:
                    i=random.randint(1,len(maze)-2)
                    j=random.randint(1,len(maze)-2)
                    #if we pick obstacle, pass
                    if maze[i][j]==1:
                        pass
                    #empty cell selected
                    else:
                        #obstacle added in blank cell
                        print(i, j)
                        maze[i][j]=1
                        mazeEdited=np.copy(maze)
                        break
            #delete obstacle
            else:
                while True:
                    m=random.randint(1,len(maze)-2)
                    n=random.randint(1,len(maze)-2)
                    #if we pick empty cell,pass
                    if maze[m][n]==0:
                        pass
                    #obstcle cell selected
                    else:
                        #obstcle deleted from obstacle cell
                        print(m, n)
                        maze[m][n]=0
                        mazeEdited=np.copy(maze)
                        break

            #call BFS with new maze
            y=BFS(mazeEdited,video=True)
            #path length of edited maze
            pathLength2=y[1]
            if pathLength2>=pathLength1:
                times_changed += 1
                return randomWalk(maze,times_changed)
            #if new path is better, call RW with edited maze
            else:
                #increase times_changed
                return randomWalk(mazeOriginal,times_changed)

