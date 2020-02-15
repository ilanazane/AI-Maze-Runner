import sys
sys.path.append('../')
from methods import *
from Algorithms.BFS import BFS
from Algorithms.DFS import DFS
from Algorithms.BiBFS import BiBFS
from Algorithms.AstarE import AstarE
from Algorithms.AstarM import AstarM

'''
***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** 
This file is purely for showing how the algorithms run via displaying the final path returned

To show off the video update, we run BiBFS through a smaller grid (to prevent the computer from having a heart attack)

Just change video = False to video = True for the below algorithms to see large grid video updates (Warning: will make computer wheeze a little)
***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** 
'''

#x, y = BFS(grid(100, 0.3), video = False) #<----- BFS Example
#x, y, z = DFS(grid(100, 0.3), video = False) #<----- DFS Example
#x, y = BiBFS(grid(100, 0.3), video = False) #<----- BiBFS Example
#x, y = AstarE(grid(100, 0.3), video = False) #<----- AstarE Example
#x, y, z = AstarM(grid(100, 0.3), video = False) #<----- AstarM Example

#make 5 copies of the same maze to be run by each algorithm
a = grid(75, 0.2)
b = np.copy(a)
c = np.copy(a)
d = np.copy(a)
e = np.copy(a)

BFS(a, video = False, show_final = True)
DFS(b, video = False, show_final = True)
BiBFS(c, video = False, show_final = True)
AstarM(d, video = False, show_final = True)
AstarE(e, video = False, show_final = True)

#demonstrate the video for BiBFS (the others are all the same... this one is the coolest)
BiBFS(grid(10, 0.2), video = True, show_final = True)
