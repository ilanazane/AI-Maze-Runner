from methods import *

#A* Manhattan Distance

def AstarM(maze, video):
    #initialize the solved state of the maze to be false and our pointers to be at the beginning
    #i controls row and j controls column
    maze_final = np.copy(maze)
    solved = False
    i, j = 0, 0
    prev = {}
    counter = 0
    
    #initialize the fringe and store the starting point of the maze
    fringe = []
    fringe.append([i, j, counter + Manhattan(maze, i, j)])
    
    
    #runs until we reach the end
    while solved == False:
        '''
        #*****this is just for debugging*****
        
        #print out the length of the current fringe
        print(queue.Queue.qsize(fringe))
            
        #looks at the queue
        for q_item in fringe.queue:
            print(q_item)
        '''
        
        #Is the maze unsolvable?
        if len(fringe) == 0:
            #update the state of the maze, display the end result, and break the loop
            update(maze, i , j)
            if video == True:
                plt.imshow(maze, cmap=plt.cm.binary)
                plt.show()
            print("UNSOLVABLE")
            #value to be returned for later analysis
            solved = 0
            solution_length = 0
            break
            
        #gets the current node and update i and j
        current = fringe.pop()
        i, j = current[0], current[1]
        
        #check if we have reached a solution, display the end result, and break the loop
        if i + 1 == len(maze) and j + 1 == len(maze[i]):
            update(maze, i , j)
            if video == True:
                plt.imshow(maze, cmap=plt.cm.binary)
                plt.pause(0.05)
            print("SOLUTION FOUND")
            #value to be returned for later analysis
            solved = 1
            
            solution_length = 0
            
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
                if [i, j - 1, counter + Manhattan(maze, i, j - 1)] in fringe:
                    pass
                else:
                    #if the fringe was empty (i.e. the first move), just add the first child to fringe
                    if len(fringe) == 0: 
                        prev[(i, j - 1)] = (i, j)
                        fringe.append((i, j - 1, counter + Manhattan(maze, i, j - 1)))
                    #if the fringe is not empty, check the f(n) value and compare with items in fringe
                    else:
                        for x in range(len(fringe)-1,-1,-1): 
                            if counter + Manhattan(maze, i, j - 1) > fringe[x][2]:
                                if x == 0:
                                    fringe.insert(0, (i, j - 1, counter + Manhattan(maze, i, j - 1)))
                                    prev[(i, j - 1)] = (i, j)
                                else:
                                    pass
                            else: 
                                fringe.insert(x + 1, (i, j - 1, counter + Manhattan(maze, i, j - 1)))
                                prev[(i, j - 1)] = (i, j)
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
                if [i - 1, j, counter + Manhattan(maze, i - 1, j)] in fringe:
                    pass
                else:
                    #if the fringe was empty (i.e. the first move), just add the first child to fringe
                    if len(fringe) == 0: 
                        prev[(i - 1, j)] = (i, j)
                        fringe.append((i - 1, j, counter + Manhattan(maze, i - 1, j)))
                    #if the fringe is not empty, check the f(n) value and compare with items in fringe
                    else:
                        for x in range(len(fringe)-1,-1,-1): 
                            if counter + Manhattan(maze, i - 1, j) > fringe[x][2]:
                                if x == 0:
                                    fringe.insert(0, (i - 1, j, counter + Manhattan(maze, i - 1, j)))
                                    prev[(i - 1, j)] = (i, j)
                                else: 
                                    pass
                            else: 
                                fringe.insert(x + 1, (i - 1, j, counter + Manhattan(maze, i - 1, j)))
                                prev[(i - 1, j)] = (i, j)
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
                if [i, j + 1, counter + Manhattan(maze, i, j + 1)] in fringe:
                    pass
                else:
                    #if the fringe was empty (i.e. the first move), just add the first child to fringe
                    if len(fringe) == 0: 
                        prev[(i, j + 1)] = (i, j)
                        fringe.append((i, j + 1, counter + Manhattan(maze, i, j + 1)))
                    #if the fringe is not empty, check the f(n) value and compare with items in fringe
                    else:
                        for x in range(len(fringe)-1,-1,-1): 
                            if counter + Manhattan(maze, i, j + 1) > fringe[x][2]:
                                if x == 0:
                                    fringe.insert(0, (i, j + 1, counter + Manhattan(maze, i, j + 1)))
                                    prev[(i, j + 1)] = (i, j)
                                else: 
                                    pass
                            else: 
                                fringe.insert(x + 1, (i, j + 1, counter + Manhattan(maze, i, j + 1)))
                                prev[(i, j + 1)] = (i, j)
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
                if [i + 1, j, counter + Manhattan(maze, i + 1, j)] in fringe:
                    pass
                else:
                    #if the fringe was empty (i.e. the first move), just add the first child to fringe
                    if len(fringe) == 0: 
                        prev[(i + 1, j)] = (i, j)
                        fringe.append((i + 1, j, counter + Manhattan(maze, i + 1, j)))
                    #if the fringe is not empty, check the f(n) value and compare with items in fringe
                    else:
                        for x in range(len(fringe)-1,-1,-1): 
                            if counter + Manhattan(maze, i + 1, j) > fringe[x][2]:
                                if x == 0:
                                    fringe.insert(0, (i + 1, j, counter + Manhattan(maze, i + 1, j)))
                                    prev[(i + 1, j)] = (i, j)
                                else: 
                                    pass
                            else: 
                                fringe.insert(x + 1, (i + 1, j, counter + Manhattan(maze, i + 1, j)))
                                prev[(i + 1, j)] = (i, j)
                                break        
        
        
        
        #after done checking, update the maze and start over
        update(maze, i, j)
        
        if video == True:
            plt.imshow(maze, cmap=plt.cm.binary)
            plt.pause(0.05)
    if video == True:
        plt.show()
        
    return solved, solution_length
    
x, y = AstarM(grid(10, 0.2), video = False)
