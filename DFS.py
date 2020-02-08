from methods import *

#DFS Search Algorithm

def DFS(maze):
    #initialize the solved state of the maze to be false and our pointers to be at the beginning
    #i controls row and j controls column
    maze_final = np.copy(maze)
    solved = False
    i, j = 0, 0
    prev = {}

    #initialize the fringe and store the starting point of the maze
    fringe = []
    fringe.append([i, j])

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
            plt.imshow(maze, cmap=plt.cm.binary)
            plt.pause(0.05)
            print("UNSOLVABLE")
            break

        #gets the current node and update i and j
        current = fringe.pop()
        i, j = current[0], current[1]

        #check if we have reached a solution, display the end result, and break the loop
        if i + 1 == len(maze) and j + 1 == len(maze[i]):
            update(maze, i , j)
            plt.imshow(maze, cmap=plt.cm.binary)
            plt.pause(0.05)
            print("SOLVED")

            update(maze_final, i, j)
            plt.imshow(maze, cmap=plt.cm.binary)
            plt.pause(0.05)

            while i != 0 or j!= 0:
                x = prev[i,j]
                i, j = x[0], x[1]
                update(maze_final, i, j)
                plt.imshow(maze_final, cmap=plt.cm.binary)
                plt.pause(0.05)

            update(maze_final, 0, 0)
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
                pass
            else:
                #add to fringe if valid and is not already in fringe
                if [i, j - 1] in fringe:
                    pass
                else:
                    prev[(i, j - 1)] = (i, j)
                    fringe.append([i, j - 1])

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
                if [i - 1, j] in fringe:
                    pass
                else:
                    prev[(i - 1, j)] = (i, j)
                    fringe.append([i - 1, j])

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
                if [i, j + 1] in fringe:
                    pass
                else:
                    prev[(i, j + 1)] = (i, j)
                    fringe.append([i, j + 1])

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
                if [i + 1, j] in fringe:
                    pass
                else:
                    prev[(i + 1, j)] = (i, j)
                    fringe.append([i + 1, j])



        #after done checking, update the maze and start over
        update(maze, i, j)

        plt.imshow(maze, cmap=plt.cm.binary)
        plt.pause(0.05)

    plt.show()

DFS(grid(10,0.2))
