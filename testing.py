from methods import *
from BFS import BFS
from DFS import DFS
from BiBFS import BiBFS
from AstarE import AstarE
from AstarM import AstarM

#x, y = BFS(grid(100, 0.3), video = False) #<----- BFS Example
#x, y, z = DFS(grid(100, 0.3), video = False) #<----- DFS Example
#x, y = BiBFS(grid(100, 0.3), video = False) #<----- BiBFS Example
#x, y = AstarE(grid(100, 0.3), video = False) #<----- AstarE Example
#x, y, z = AstarM(grid(100, 0.3), video = False) #<----- AstarM Example

#make 5 copies of the same maze to be run by each algorithm
a = grid(100, 0.2)
b = np.copy(a)
c = np.copy(a)
d = np.copy(a)
e = np.copy(a)

BFS(a, video = False)
DFS(b, video = False)
BiBFS(c, video = False)
AstarM(d, video = False)
AstarE(e, video = False)
