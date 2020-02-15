import sys
sys.path.append('../')
from methods import *
from Algorithms.AstarM import AstarM
from Algorithms.DFS import DFS

#HILLCLIMB WITH AstarM

#maze is filled with empty cells and obstacles
def hillClimbAstarM(maze,consec_fails):
    print('fails',consec_fails)
    #if more than 10 consecutive fails, we have reached local maxima
    if consec_fails > np.sqrt(len(maze)):
        plt.imshow(maze, cmap=plt.cm.binary)
        plt.show()
        return maze
    else:
        mazeOriginal=np.copy(maze)
        maze2 = np.copy(maze)
        #call AstarM with original maze
        algo1=AstarM(maze2,video=False, show_final = False)
        #all nodes explored with original maze is stored into maxNode1
        maxNode1=algo1[2]
        #if AstarM is solvable
        if algo1[0]==1:
            y=random.random()
            #add obstacle
            while True:
                #find a cell at i,j
                i=random.randint(1,len(maze)-2)
                j=random.randint(1,len(maze)-2)
                #if we pick a cell that already has obstacle, pass
                if maze[i][j]==1:
                    pass
                #if we pick an empty cell
                else:
                    #obstacle added in empty cell
                    maze[i][j]=1
                    mazeEdited=np.copy(maze)
                    break

            #call AstarM with new maze
            algo2=AstarM(mazeEdited,video=False, show_final = False)
            #all nodes explored of edited maze
            maxNode2=algo2[2]
            #if manxNode of edited maze is more than that of original maze
            #and AstarM of edited maze is solvable, hillClimb with edited maze
            if maxNode2>=maxNode1 and algo2[0] == 1:
                consec_fails=0
                return hillClimbAstarM(maze,consec_fails)
            else:
                #increase consecutive fails
                consec_fails+=1
                return hillClimbAstarM(mazeOriginal,consec_fails)
    print('no solution, try again (initial maze failure)')


#HILLCLIMB WITH DFS
#maze is filled with empty and obstacles
def hillClimbDFS(maze, consec_fails):
    print(consec_fails)
    #if there are more than 10 consistent fails, local maxima reached
    if consec_fails > np.sqrt(len(maze)):
        plt.imshow(maze, cmap=plt.cm.binary)
        plt.show()
        return maze
    else:
        mazeOriginal=np.copy(maze)
        maze2 = np.copy(maze)
        #call DFS with original maze
        algo1=DFS(maze2,video=False, show_final = False)
        fringeSize1=algo1[2]
        #if DFS is solvable
        if algo1[0]==1:
            y=random.random()
            #add obstacle
            while True:
                #find a cell at i,j
                i=random.randint(1,len(maze)-2)
                j=random.randint(1,len(maze)-2)
                #if we pick obstacle, pass
                if maze[i][j]==1:
                    pass
                #empty cell selected
                else:
                    #obstacle added in blank cell
                    maze[i][j]=1
                    mazeEdited=np.copy(maze)
                    break

            #call DFS with edited maze
            algo2=DFS(mazeEdited,video=False, show_final = False)
            #path length of edited maze
            fringeSize2=algo2[2]
            #if fringe of edited maze is bigger than fringe of original
            if fringeSize2>=fringeSize1:
                consec_fails = 0
                #continue hillClimb with edited maze as new original
                return hillClimbDFS(maze,consec_fails)
            else:
                #increase fails
                consec_fails += 1
                #continue hillClimb with original maze
                return hillClimbDFS(mazeOriginal,consec_fails)
    print('no solution, try again (initial maze failure)')
