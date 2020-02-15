from firemethods import *

'''
A* firemanhattan Search Algorithm
            **inputs**
-maze = a dim x dim array to be worked with
-video = boolean variable to either show a live update of the maze or not
-show_final = boolean variable to either display the final solution or not
            **returns**

-solved = 1 if solved, 0 if not
-solution_length = integer value of the final solution length
-maxNode = the total number of nodes expanded, to be used for local search
x, y, z = AstarM(100, 0.3), video = False) #<----- AstarM Example
'''

def fireAstarM(maze, q, video, show_final):
    #initialize the solved state of the maze to be false and our pointers to be at the beginning
    #i controls row and j controls column
    solved = False
    onFire = False
    i, j = 0, 0
    #make a copy of the maze to be used to reconstruct the final path once a solution is found
    maze_final = np.copy(maze)
    #create a dictionary called prev to point to previous positions
    prev = {}
    #establish a counter to keep track of the number of moves made so far (is g(n))
    counter = 0
    #all nodes explored. initialize to 0
    maxNode=0

    #initialize the fringe and store the starting point of the maze
    fringe = []
    fringe.append((i, j, counter + firemanhattan(maze, i, j, q)))

    if video == True:
        plt.imshow(maze, cmap=plt.cm.binary)
        plt.pause(0.05)

    #runs until we reach the end
    while solved == False and onFire == False:
        #check if ij is on fire
        if maze[i][j]==0.75:
            onFire=True
            print("U BURNED")
            solved = 0
            solution_length = 0
            break


        #Is the maze unsolvable?
        if len(fringe) == 0:
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

        #gets the current node and update i and j; update counter
        current = fringe.pop()

        #every time a node is explored, increase maxNode by 1
        maxNode += 1
        i, j = current[0], current[1]
        counter = current[2] - firemanhattan(maze, i, j, q) + 1

        #check if we have reached a solution, if so, display the end result and break the loop
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
            if maze[i][j - 1] == 1 or maze[i][j - 1] == 0.5 or maze[i][j - 1] == 0.75:
                #If so, move on
                pass
            else:
                #check if already in fringe
                if (i, j - 1, counter + firemanhattan(maze, i, j - 1,q)) in fringe:
                    pass
                else:
                    #if the fringe was empty (i.e. the first move), just add the first child to fringe
                    if len(fringe) == 0:
                        prev[(i, j - 1, counter + firemanhattan(maze, i, j - 1,q))] = (i, j, counter - 1 + firemanhattan(maze, i, j,q))
                        fringe.append((i, j - 1, counter + firemanhattan(maze, i, j - 1,q)))
                    #if the fringe is not empty, check the f(n) value and compare with items in fringe
                    else:

                        for x in range(len(fringe)-1,-1,-1):
                            if counter + firemanhattan(maze, i, j - 1,q) > fringe[x][2]:
                                if x == 0:
                                    fringe.insert(0, (i, j - 1, counter + firemanhattan(maze, i, j - 1,q)))
                                    prev[(i, j - 1, counter + firemanhattan(maze, i, j - 1,q))] = (i, j, counter - 1 + firemanhattan(maze, i, j,q))
                                else:
                                    pass
                            else:
                                fringe.insert(x + 1, (i, j - 1, counter + firemanhattan(maze, i, j - 1,q)))
                                prev[(i, j - 1, counter + firemanhattan(maze, i, j - 1,q))] = (i, j, counter - 1 + firemanhattan(maze, i, j,q))
                                break

        #check up solution

        #are we outside?
        if i - 1 < 0:
            pass
        else:
            #is the next position occupied or previously visited?
            if maze[i - 1][j] == 1 or maze[i - 1][j] == 0.5 or maze[i - 1][j] == 0.75:
                pass
            else:
                #check if already in fringe
                if (i - 1, j, counter + firemanhattan(maze, i - 1, j,q)) in fringe:
                    pass
                else:
                    #if the fringe was empty (i.e. the first move), just add the first child to fringe
                    if len(fringe) == 0:
                        prev[(i - 1, j, counter + firemanhattan(maze, i - 1, j,q))] = (i, j, counter - 1 + firemanhattan(maze, i, j,q))
                        fringe.append((i - 1, j, counter + firemanhattan(maze, i - 1, j, q)))
                    #if the fringe is not empty, check the f(n) value and compare with items in fringe
                    else:
                        for x in range(len(fringe)-1,-1,-1):
                            if counter + firemanhattan(maze, i - 1, j, q) > fringe[x][2]:
                                if x == 0:
                                    fringe.insert(0, (i - 1, j, counter + firemanhattan(maze, i - 1, j, q)))
                                    prev[(i - 1, j, counter + firemanhattan(maze, i - 1, j, q))] = (i, j, counter - 1 + firemanhattan(maze, i, j, q))
                                else:
                                    pass
                            else:
                                fringe.insert(x + 1, (i - 1, j, counter + firemanhattan(maze, i - 1, j, q)))
                                prev[(i - 1, j, counter + firemanhattan(maze, i - 1, j, q))] = (i, j, counter - 1 + firemanhattan(maze, i, j, q))
                                break

        #check right position

        #are we outside?
        if j + 1 >= len(maze[i]):
            pass
        else:
            #is the next position occupied or previously visited?
            if maze[i][j + 1] == 1 or maze[i][j + 1] == 0.5 or maze[i][j + 1] == 0.75:
                pass
            else:
                #check if already in fringe
                if (i, j + 1, counter + firemanhattan(maze, i, j + 1, q)) in fringe:
                    pass
                else:
                    #if the fringe was empty (i.e. the first move), just add the first child to fringe
                    if len(fringe) == 0:
                        prev[(i, j + 1, counter + firemanhattan(maze, i, j + 1, q))] = (i, j, counter - 1 + firemanhattan(maze, i, j, q))
                        fringe.append((i, j + 1, counter + firemanhattan(maze, i, j + 1, q)))
                    #if the fringe is not empty, check the f(n) value and compare with items in fringe
                    else:
                        for x in range(len(fringe)-1,-1,-1):
                            if counter + firemanhattan(maze, i, j + 1, q) > fringe[x][2]:
                                if x == 0:
                                    fringe.insert(0, (i, j + 1, counter + firemanhattan(maze, i, j + 1, q)))
                                    prev[(i, j + 1, counter + firemanhattan(maze, i, j + 1, q))] = (i, j, counter - 1 + firemanhattan(maze, i, j, q))
                                else:
                                    pass
                            else:
                                fringe.insert(x + 1, (i, j + 1, counter + firemanhattan(maze, i, j + 1,q)))
                                prev[(i, j + 1, counter + firemanhattan(maze, i, j + 1, q))] = (i, j, counter - 1 + firemanhattan(maze, i, j, q))
                                break

        #check down position

        #are we outside?
        if i + 1 >= len(maze):
            pass
        else:
            #is the next position occupied or previously visited?
            if maze[i + 1][j] == 1 or maze[i + 1][j] == 0.5 or maze[i + 1][j] == 0.75:
                pass
            else:
                #check if already in fringe
                if (i + 1, j, counter + firemanhattan(maze, i + 1, j, q)) in fringe:
                    pass
                else:
                    #if the fringe was empty (i.e. the first move), just add the first child to fringe
                    if len(fringe) == 0:
                        prev[(i + 1, j, counter + firemanhattan(maze, i + 1, j, q))] = (i, j, counter - 1 + firemanhattan(maze, i, j, q))
                        fringe.append((i + 1, j, counter + firemanhattan(maze, i + 1, j, q)))
                    #if the fringe is not empty, check the f(n) value and compare with items in fringe
                    else:
                        for x in range(len(fringe)-1,-1,-1):
                            if counter + firemanhattan(maze, i + 1, j, q) > fringe[x][2]:
                                if x == 0:
                                    fringe.insert(0, (i + 1, j, counter + firemanhattan(maze, i + 1, j, q)))
                                    prev[(i + 1, j, counter + firemanhattan(maze, i + 1, j, q))] = (i, j, counter - 1 + firemanhattan(maze, i, j, q))
                                else:
                                    pass
                            else:
                                fringe.insert(x + 1, (i + 1, j, counter + firemanhattan(maze, i + 1, j, q)))
                                prev[(i + 1, j, counter + firemanhattan(maze, i + 1, j, q))] = (i, j, counter - 1 + firemanhattan(maze, i, j, q))
                                break


        #after done checking, update the maze and keep going
        updateFire(maze, q)
        update(maze, i, j)


        if video == True:
            plt.imshow(maze, cmap=plt.cm.binary)
            plt.pause(0.05)

    if show_final == True:
           plt.figure(figsize=(10,10))
           plt.title("AstarM", fontsize = 40)
           plt.imshow(maze_final, cmap=plt.cm.binary)
           plt.show()

    return solved, solution_length, maxNode

fireAstarM(firegrid(10, 0.2), 0.1, video = True, show_final = False)
