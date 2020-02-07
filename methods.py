#Functions that will be very useful for creating/updating mazes

'''
Define the grid to be working with

            **inputs**

-dim = dimension size of the grid 
-p = probability that a grid spot will be filled or open
'''

def grid(dim, p):
    #start with a dim by dim zero array
    a = np.zeros((dim,dim))
    for item in range(dim):
        for thing in range(dim):
            #makes sure the top left spot is empty
            if item == 0 and thing == 0:
                pass
            #makes sure the bottom right spot is empty
            elif item == dim - 1 and thing == dim - 1:
                pass
            #change the cells based off of the value of p and our random number
            else:
                x = random.random()
                #if our random number is less than p, then the cell will not be filled
                if p < x:
                    a[item][thing] = 0
                #if our random number is greater than p, then the cell will  be filled
                else:
                    a[item][thing] = 1
    
    #plots the initial state of the maze 
    plt.figure(figsize=(5,5))
    plt.imshow(a, cmap=plt.cm.binary)
    plt.show()
    time.sleep(2)
    return a


'''
update the state of the maze after moving to the next tile

            **inputs**

-maze = the maze to be updated
-i = which row to update
-j = which column to update
'''
def update(maze, i, j):
    #shades the tile grey to distinguish between open and occupied
    maze[i][j] = 0.5
