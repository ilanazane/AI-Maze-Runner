import sys
sys.path.append('../')
from methods import *
from Algorithms.AstarM import AstarM
from Algorithms.DFS import DFS
from Local_Search.hillClimbAstarM import hillClimbAstarM
from Local_Search.hillClimbDFS import hillClimbDFS

'''
***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** 
This file is showing off the local search algorithms
Each hill climbing algorithm is run on the same mazes, and the before and afters are displayed

hillClimbDFS will try to maximize the total fringe size
hillCLimbAstarM will try to maximize the total nodes explored
***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** 
'''

a = grid(30, 0.2)
b = np.copy(a)
c = np.copy(a)
d = np.copy(a)

#show initial path returned by DFS
DFS(a, video = False, show_final = True)
#hill climb
harder_DFS_maze = hillClimbDFS(b, 0)
#show the final path returned by DFS
DFS(harder_DFS_maze, video = False, show_final = True)

#show initial path returned by AstarM
AstarM(c, video = False, show_final = True)
#hill climb
harder_AstarM_maze = hillClimbAstarM(d, 0)
#show the final path returned by AstarM
AstarM(harder_AstarM_maze, video = False, show_final = True)
