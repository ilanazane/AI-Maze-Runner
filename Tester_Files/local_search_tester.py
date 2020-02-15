from methods import *
from Algorithms.AstarM import AstarM
from Algorithms.DFS import DFS
from Local_Search.hillClimbAstarM import hillClimbAstarM
from Local_Search.hillClimbDFS import hillClimbDFS

a = grid(75, 0.2)
b = np.copy(a)

harder_DFS_maze = hillClimbDFS(a, 0)
harder_AstarM_maze = hillClimb(b, 0)
