#HILLCLIMB WITH DFS 
#maze is filled with empty and obstacles
def hillClimb(maze, consec_fails):
    print(consec_fails)
    #if there are more than 10 consistent fails, local maxima reached 
    if consec_fails > 10:
        print('hi dfs')
        return maze
    else:
        mazeOriginal=np.copy(maze)
        maze2 = np.copy(maze)
        #call DFS with original maze
        algo1=DFS(maze2,video=False)
        fringeSize1=algo1[2]
        #if DFS is solvable
        if algo1[0]==1:
            y=random.random()
            #add obstacle
            if y > 0:
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
                        
                        
            #delete obstacle
            #else:
            #    while True:
            #        m=random.randint(1,len(maze)-2)
            #        n=random.randint(1,len(maze)-2)
            #        #if we pick empty cell,pass
            #        if maze[m][n]==0:
            #            pass
            #        #obstcle cell selected
            #        else:
            #            #obstcle deleted from obstacle cell
            #            maze[m][n]=0
            #            mazeEdited=np.copy(maze)
            #            break
            
            #call DFS with edited maze
            algo2=DFS(mazeEdited,video=False)
            #path length of edited maze
            fringeSize2=algo2[2]
            print(fringeSize1, fringeSize2)
            #if fringe of edited maze is bigger than fringe of original 
            if fringeSize2>=fringeSize1:
                consec_fails = 0
                #continue hillClimb with edited maze as new original 
                return hillClimb(maze,consec_fails)
            else:
                #increase fails 
                consec_fails += 1
                #continue hillClimb with original maze 
                return hillClimb(mazeOriginal,consec_fails)
    print('no solution')

a=randomWalk(grid(20,0.3),0)
