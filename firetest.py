from firemethods import *
#from DFS import DFS
#from BiBFS import BiBFS
#from AstarE import AstarE
from fireAstarM import fireAstarM

#x, y = BFS(grid(100, 0.3), video = False) #<----- BFS Example
#x, y, z = DFS(grid(100, 0.3), video = False) #<----- DFS Example
#x, y = BiBFS(grid(100, 0.3), video = False) #<----- BiBFS Example
#x, y = AstarE(grid(100, 0.3), video = False) #<----- AstarE Example
#x, y, z = AstarM(grid(100, 0.3), video = False) #<----- AstarM Example

#make 5 copies of the same maze to be run by each algorithm
a = firegrid(10, 0.2)
b = np.copy(a)
c = np.copy(a)
d = np.copy(a)
e = np.copy(a)

#BFS(a, video = False)
#DFS(b, video = False)
fireAstarM(d, video = True, show_final = True)
#AstarE(e, video = False)
