import sys
sys.path.append('../')
from methods import *
from Algorithms.AstarM import AstarM

#HILLCLIMB WITH AstarM

#maze is filled with empty cells and obstacles
def hillClimbAstarM(maze,consec_fails):
    print('fails',consec_fails)
    #if more than 10 consecutive fails, we have reached local maxima
    if consec_fails > np.sqrt(len(maze)):
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
    return []
