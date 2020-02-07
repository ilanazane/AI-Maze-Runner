from methods import *
#bidirectional bfs algorithm
def BiBFS(maze):
#initialized state is set to false
#i,j-->row,column from start m,n-->row,column from end
    maze_final=np.copy(maze)
    solved=False
    i,j=0,0
    m,n=len(maze)-1,len(maze[0])-1
    prev={}
#initialize fringe for starting point and fringe from ending point
    fringeStart=queue.Queue()
    fringeStart.put([i,j])
    fringeEnd=queue.Queue()
    fringeEnd.put([m,n])
#run loop until start and end meet
    while solved==False:
#if maze is still unsolved and there are no more children left in fringe, maze is unsolvable
        if (queue.Queue.qsize(fringeStart)==0 or queue.Queue.qsize(fringeEnd)==0):
#update state of maze, display result, then break loop
            update(maze,i,j)
            update(maze,m,n)
            plt.figure(figsize=(5,5))
            plt.imshow(maze,cmap=plt.cm.binary)
            plt.show()
            print("UNSOLVABLE")
            break
#gets current node and updates i,j and m,n
        currentStart=fringeStart.get()
        currentEnd=fringeEnd.get()
        i,j=currentStart[0],currentStart[1]
        m,n=currentEnd[0],currentEnd[1]
    #check if start and end meet in middle,display result, then break loop
        if (i==m and j+1==n)or(i+1==m and j==n)or(i==m and j==n):
            update(maze,i,j)
            update(maze,m,n)
            plt.figure(figsize=(5,5))
            plt.imshow(maze,cmap=plt.cm.binary)
            plt.show()
            print("SOLVED")

            update(maze_final,i,j)
            update(maze_final,m,n)

            while (i!=0 or j!=0) and (m!=0 or n!=0):
                x=prev[(i,j)]
                y=prev[(m,n)]
                i,j=x[0],x[1]
                m,n=y[0],y[1]
                update(maze_final,i,j)
                update(maze_final,m,n)

            update(maze_final,0,0)
            update(maze_final,len(maze)-1,len(maze[0])-1)

            break
#check down position of i,j
        if i + 1 >= len(maze):
            pass
        else:
            #is the next position occupied or previously visited?
            if maze[i + 1][j] == 1 or maze[i + 1][j] == 0.5:
                pass
            else:
                #add to fringe if valid and is not already in fringe
                if [i + 1, j] in fringeStart.queue:
                    pass
                else:
                    prev[(i + 1, j)] = (i, j)
                    fringeStart.put([i + 1, j])
#check up position of m,n
        if m - 1 < 0:
            pass
        else:
            #is the next position occupied or previously visited?
            if maze[m - 1][n] == 1 or maze[m - 1][n] == 0.5:
                pass
            else:
                #add to fringe if valid and is not already in fringe
                if [n - 1, n] in fringeEnd.queue:
                    pass
                else:
                    prev[(m - 1, n)] = (m, n)
                    fringeEnd.put([m - 1, n])
#check right position of i,j
        if j + 1 >= len(maze[i]):
            pass
        else:
            #is the next position occupied or iously visited?
            if maze[i][j + 1] == 1 or maze[i][j + 1] == 0.5:
                pass
            else:
                #add to fringe if valid and is not already in fringe
                if [i, j + 1] in fringeStart.queue:
                    pass
                else:
                    prev [(i, j + 1)] = (i, j)
                    fringeStart.put([i, j + 1])
#check left position of m,n
        if n - 1 < 0:
            pass
        else:
            #is the next position occupied or previously visited?
            if maze[m][n - 1] == 1 or maze[m][n - 1] == 0.5:
                pass
            else:
                #add to fringe if valid and is not already in fringe
                if [m, n - 1] in fringeEnd.queue:
                    pass
                else:
                    prev[(m, n - 1)] = (m, n)
                    fringeEnd.put([m, n - 1])
#check up position of i,j
        if i - 1 < 0:
            pass
        else:
            #is the next position occupied or previously visited?
            if maze[i - 1][j] == 1 or maze[i - 1][j] == 0.5:
                pass
            else:
                #add to fringe if valid and is not already in fringe
                if [i - 1, j] in fringeStart.queue:
                    pass
                else:
                    prev[(i - 1, j)] = (i, j)
                    fringeStart.put([i - 1, j])
#check down position of m,n
        if m + 1 >= len(maze):
            pass
        else:
            #is the next position occupied or previously visited?
            if maze[m + 1][n] == 1 or maze[m + 1][n] == 0.5:
                pass
            else:
                #add to fringe if valid and is not already in fringe
                if [m + 1, n] in fringeEnd.queue:
                    pass
                else:
                    prev[(m + 1, n)] = (m, n)
                    fringeEnd.put([m + 1, n])
#check left position of i,j
        if j - 1 < 0:
            pass
        else:
            #is the next position occupied or previously visited?
            if maze[i][j - 1] == 1 or maze[i][j - 1] == 0.5:
                pass
            else:
                #add to fringe if valid and is not already in fringe
                if [i, j - 1] in fringeStart.queue:
                    pass
                else:
                    prev[(i, j - 1)] = (i, j)
                    fringeStart.put([i, j - 1])
#check right position of m,n
        if n + 1 >= len(maze[m]):
            pass
        else:
            #is the next position occupied or previously visited?
            if maze[m][n + 1] == 1 or maze[m][n + 1] == 0.5:
                pass
            else:
                #add to fringe if valid and is not already in fringe
                if [m, n + 1] in fringeEnd.queue:
                    pass
                else:
                    prev[(m, n + 1)] = (m, n)
                    fringeEnd.put([m, n + 1])
#after done checking, update maze and start over
        update(maze, i, j)
        update(maze,m,n)
#test bidirection bfs
BiBFS(grid(10,0.2))
