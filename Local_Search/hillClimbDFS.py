import sys
sys.path.append('../')
from methods import *
from Algorithms.DFS import DFS

#HILLCLIMB WITH DFS
#maze is filled with empty and obstacles
def hillClimbDFS(maze, consec_fails):
    print(consec_fails)
    #if there are more than 10 consistent fails, local maxima reached
    if consec_fails > np.sqrt(len(maze)):
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
    return []
