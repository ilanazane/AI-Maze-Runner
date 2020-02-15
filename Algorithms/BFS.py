import sys
sys.path.append('../')
from methods import *

'''
BFS Search Algorithm

            **inputs**

-maze = a dim x dim array to be worked with
-video = boolean variable to either show a live update of the maze or not
-show_final = boolean variable to either display the final solution or not

            **returns**
            
-solved = 1 if solved, 0 if not
-solution_length = integer value of the final solution length

x, y = BFS(grid(100, 0.3), video = False, show_final = True) #<----- BFS Example
'''

def BFS(maze, video, show_final):
    #initialize the solved state of the maze to be false and our pointers, i and j, to be at the beginning
    #i controls row and j controls column
    solved = False
    i, j = 0, 0
    #make a copy of the maze to be used to reconstruct the final path once a solution is found
    maze_final = np.copy(maze)
    #create a dictionary called prev to point to previous positions
    prev = {}
    
    #initialize the fringe (a queue) and store the starting point of the maze
    fringe = queue.Queue()
    fringe.put((i, j))
    
    if video == True:
        plt.imshow(maze, cmap=plt.cm.binary)
        plt.pause(0.05)
    
    #runs until we reach the end
    while solved == False:
        #Is the maze unsolvable?
        if queue.Queue.qsize(fringe) == 0:
            #update the state of the maze, display the end result, and break the loop
            update(maze, i , j)
            if video == True:
                plt.imshow(maze, cmap=plt.cm.binary)
                plt.pause(0.05)
            print("UNSOLVABLE")
            #set the values of solved and solution_length to be zero
            solved = 0
            solution_length = 0
            break
        
        #gets the current node and update i and j
        current = fringe.get()
        i, j = current[0], current[1]
        
        #check if we have reached a solution, if so, display the end result and break the loop
        if i + 1 == len(maze) and j + 1 == len(maze[i]):
            update(maze, i , j)
            if video == True:
                plt.imshow(maze, cmap=plt.cm.binary)
                plt.pause(0.05)
            print("SOLUTION FOUND")
            #set the values of solved to one and initialize solution_length to be zero
            solved = 1
            solution_length = 0
    
            #start to reconstruct the path back and increment solution_length
            update(maze_final, i, j)
            if video == True:
                plt.imshow(maze, cmap=plt.cm.binary)
                plt.pause(0.05)
                
            while i != 0 or j!= 0:
                x = prev[i,j]
                i, j = x[0], x[1]
                update(maze_final, i, j)
                if video == True:
                    plt.imshow(maze_final, cmap=plt.cm.binary)
                    plt.pause(0.05)
                solution_length += 1
            
            update(maze_final, 0, 0)
            if video == True:
                plt.imshow(maze_final, cmap=plt.cm.binary)
                plt.pause(0.05)
            
            break
        
        #check down position
        
        #are we outside?
        if i + 1 >= len(maze):
            pass
        else:
            #is the next position occupied or previously visited?
            if maze[i + 1][j] == 1 or maze[i + 1][j] == 0.5:
                pass
            else:
                #add to fringe if valid and is not already in fringe
                if [i + 1, j] in fringe.queue:
                    pass
                else:
                    prev[(i + 1, j)] = (i, j)
                    fringe.put([i + 1, j])

        #check right position
        
        #are we outside?
        if j + 1 >= len(maze[i]):
            pass
        else:
            #is the next position occupied or previously visited?
            if maze[i][j + 1] == 1 or maze[i][j + 1] == 0.5:
                pass
            else:
                #add to fringe if valid and is not already in fringe
                if [i, j + 1] in fringe.queue:
                    pass
                else:
                    prev[(i, j + 1)] = (i, j)
                    fringe.put([i, j + 1])
        
        #check up solution
        
        #are we outside?
        if i - 1 < 0:
            pass
        else:
            #is the next position occupied or previously visited?
            if maze[i - 1][j] == 1 or maze[i - 1][j] == 0.5:
                pass
            else:
                #add to fringe if valid and is not already in fringe
                if [i - 1, j] in fringe.queue:
                    pass
                else:
                    prev[(i - 1, j)] = (i, j)
                    fringe.put([i - 1, j])
        
        #check left solution
        
        #are we outside?
        if j - 1 < 0:
            pass
        else:
            #is the next position occupied or previously visited?
            if maze[i][j - 1] == 1 or maze[i][j - 1] == 0.5:
                pass
            else:
                #add to fringe if valid and is not already in fringe
                if [i, j - 1] in fringe.queue:
                    pass
                else:
                    prev[(i, j - 1)] = (i, j)
                    fringe.put([i, j - 1])
        
        
        #after done checking, update the maze and keep going
        update(maze, i, j)
    
        if video == True:
            plt.imshow(maze, cmap=plt.cm.binary)
            plt.pause(0.05)
    
    if show_final == True:
           plt.figure(figsize=(10,10))
           plt.title("BFS", fontsize = 40)
           plt.imshow(maze_final, cmap=plt.cm.binary)
           plt.show()
    
    return solved, solution_length
