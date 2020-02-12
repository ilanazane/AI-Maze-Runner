from methods import *
from BFS import *

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
