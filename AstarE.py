from methods import *

'''
A* Euclidean Search Algorithm

            **inputs**

-maze = a dim x dim array to be worked with
-video = boolean variable to either show a live update of the maze or not

            **returns**
            
-solved = 1 if solved, 0 if not
-solution_length = integer value of the final solution length

x, y, z = AstarE(grid(100, 0.3), video = False) #<----- AstarE Example
'''

def AstarE(maze, video):
    #initialize the solved state of the maze to be false and our pointers to be at the beginning
    #i controls row and j controls column
    solved = False
    i, j = 0, 0
    #make a copy of the maze to be used to reconstruct the final path once a solution is found
    maze_final = np.copy(maze)
    #create a dictionary called prev to point to previous positions
    prev = {}
    #establish a counter to keep track of the number of moves made so far (is g(n))
    counter = 0
    
    #initialize the fringe and store the starting point of the maze
    fringe = []
    fringe.append((i, j, counter + Euclidean(maze, i, j)))
    
    if video == True:
        plt.imshow(maze, cmap=plt.cm.binary)
        plt.pause(0.05)
        
    #runs until we reach the end
    while solved == False:    
        #Is the maze unsolvable?
        if len(fringe) == 0:
            #update the state of the maze, display the end result, and break the loop
            update(maze, i , j)
            if video == True:
                plt.imshow(maze, cmap=plt.cm.binary)
                plt.show()
            print("UNSOLVABLE")
            #set the values of solved and solution_length to be zero
            solved = 0
            solution_length = 0
            break
            
        #gets the current node and update i and j
        current = fringe.pop()
        i, j = current[0], current[1]
        counter = current[2] - Euclidean(maze, i, j) + 1
        
        #check if we have reached a solution, display the end result, and break the loop
        if i + 1 == len(maze) and j + 1 == len(maze[i]):
            moves = current[2]
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
                x = prev[i,j, moves]
                i, j, moves = x[0], x[1], x[2]
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
       
        #check left solution
        
        #are we outside?
        
        if j - 1 < 0:
            pass
        else:
            #is the next position occupied or previously visited?
            if maze[i][j - 1] == 1 or maze[i][j - 1] == 0.5:
                #If so, move on
                pass
            else:
                #check if already in fringe
                if (i, j - 1, counter + Euclidean(maze, i, j - 1)) in fringe:
                    pass
                else:
                    #if the fringe was empty (i.e. the first move), just add the first child to fringe
                    if len(fringe) == 0: 
                        prev[(i, j - 1, counter + Euclidean(maze, i, j - 1))] = (i, j, counter - 1 + Euclidean(maze, i, j))
                        fringe.append((i, j - 1, counter + Euclidean(maze, i, j - 1)))
                    #if the fringe is not empty, check the f(n) value and compare with items in fringe
                    else:
                        for x in range(len(fringe)-1,-1,-1): 
                            if counter + Euclidean(maze, i, j - 1) > fringe[x][2]:
                                if x == 0:
                                    fringe.insert(0, (i, j - 1, counter + Euclidean(maze, i, j - 1)))
                                    prev[(i, j - 1, counter + Euclidean(maze, i, j - 1))] = (i, j, counter - 1 + Euclidean(maze, i, j))
                                else:
                                    pass
                            else: 
                                fringe.insert(x + 1, (i, j - 1, counter + Euclidean(maze, i, j - 1)))
                                prev[(i, j - 1, counter + Euclidean(maze, i, j - 1))] = (i, j, counter - 1 + Euclidean(maze, i, j))
                                break 
                    
        #check up solution
        
        #are we outside?
        if i - 1 < 0:
            pass
        else:
            #is the next position occupied or previously visited?
            if maze[i - 1][j] == 1 or maze[i - 1][j] == 0.5:
                pass
            else:
                #check if already in fringe
                if (i - 1, j, counter + Euclidean(maze, i - 1, j)) in fringe:
                    pass
                else:
                    #if the fringe was empty (i.e. the first move), just add the first child to fringe
                    if len(fringe) == 0: 
                        prev[(i - 1, j, counter + Euclidean(maze, i - 1, j))] = (i, j, counter - 1 + Euclidean(maze, i, j))
                        fringe.append((i - 1, j, counter + Euclidean(maze, i - 1, j)))
                    #if the fringe is not empty, check the f(n) value and compare with items in fringe
                    else:
                        for x in range(len(fringe)-1,-1,-1): 
                            if counter + Euclidean(maze, i - 1, j) > fringe[x][2]:
                                if x == 0:
                                    fringe.insert(0, (i - 1, j, counter + Euclidean(maze, i - 1, j)))
                                    prev[(i - 1, j, counter + Euclidean(maze, i - 1, j))] = (i, j, counter - 1 + Euclidean(maze, i, j))
                                else: 
                                    pass
                            else: 
                                fringe.insert(x + 1, (i - 1, j, counter + Euclidean(maze, i - 1, j)))
                                prev[(i - 1, j, counter + Euclidean(maze, i - 1, j))] = (i, j, counter - 1 + Euclidean(maze, i, j))
                                break
                                
        #check right position
        
        #are we outside?
        if j + 1 >= len(maze[i]):
            pass
        else:
            #is the next position occupied or previously visited?
            if maze[i][j + 1] == 1 or maze[i][j + 1] == 0.5:
                pass
            else:
                #check if already in fringe
                if (i, j + 1, counter + Euclidean(maze, i, j + 1)) in fringe:
                    pass
                else:
                    #if the fringe was empty (i.e. the first move), just add the first child to fringe
                    if len(fringe) == 0: 
                        prev[(i, j + 1, counter + Euclidean(maze, i, j + 1))] = (i, j, counter - 1 + Euclidean(maze, i, j))
                        fringe.append((i, j + 1, counter + Euclidean(maze, i, j + 1)))
                    #if the fringe is not empty, check the f(n) value and compare with items in fringe
                    else:
                        for x in range(len(fringe)-1,-1,-1): 
                            if counter + Euclidean(maze, i, j + 1) > fringe[x][2]:
                                if x == 0:
                                    fringe.insert(0, (i, j + 1, counter + Euclidean(maze, i, j + 1)))
                                    prev[(i, j + 1, counter + Euclidean(maze, i, j + 1))] = (i, j, counter - 1 + Euclidean(maze, i, j))
                                else: 
                                    pass
                            else: 
                                fringe.insert(x + 1, (i, j + 1, counter + Euclidean(maze, i, j + 1)))
                                prev[(i, j + 1, counter + Euclidean(maze, i, j + 1))] = (i, j, counter - 1 + Euclidean(maze, i, j))
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
                #check if already in fringe
                if (i + 1, j, counter + Euclidean(maze, i + 1, j)) in fringe:
                    pass
                else:
                    #if the fringe was empty (i.e. the first move), just add the first child to fringe
                    if len(fringe) == 0: 
                        prev[(i + 1, j, counter + Euclidean(maze, i + 1, j))] = (i, j, counter - 1 + Euclidean(maze, i, j))
                        fringe.append((i + 1, j, counter + Euclidean(maze, i + 1, j)))
                    #if the fringe is not empty, check the f(n) value and compare with items in fringe
                    else:
                        for x in range(len(fringe)-1,-1,-1): 
                            if counter + Euclidean(maze, i + 1, j) > fringe[x][2]:
                                if x == 0:
                                    fringe.insert(0, (i + 1, j, counter + Euclidean(maze, i + 1, j)))
                                    prev[(i + 1, j, counter + Euclidean(maze, i + 1, j))] = (i, j, counter - 1 + Euclidean(maze, i, j))
                                else: 
                                    pass
                            else: 
                                fringe.insert(x + 1, (i + 1, j, counter + Euclidean(maze, i + 1, j)))
                                prev[(i + 1, j, counter + Euclidean(maze, i + 1, j))] = (i, j, counter - 1 + Euclidean(maze, i, j))
                                break        
        
        #after done checking, update the maze and keep going
        update(maze, i, j)
        
        if video == True:
            plt.imshow(maze, cmap=plt.cm.binary)
            plt.pause(0.05)

    plt.figure(figsize=(10,10))
    plt.title("AstarE", fontsize = 40)
    plt.imshow(maze_final, cmap=plt.cm.binary)
    plt.show()
        
    return solved, solution_length
