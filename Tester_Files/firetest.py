import sys
sys.path.append('../')
from methods import *
from Maze_On_Fire.fire1 import fire1
from Maze_On_Fire.fire2 import fire2
from Maze_On_Fire.fire3 import fire3

'''
***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** 
For running the different strategies on the same mazes 
-fire will still spread differently for each maze, but starting position is the same
***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** 
'''

#make copies of the same maze to be run by each algorithm
a = firegrid(15, 0.2)
b = np.copy(a)
c = np.copy(a)

print("Strategy 1: Regular A*Manhattan")
time.sleep(2)
fire1(a, video = True, show_final = False, q = 0.1)
print()
print("Strategy 2: Adapt to Environment")
time.sleep(2)
fire2(b, video = True, show_final = False, q = 0.1)
print()
print("Strategy 3: Plan Ahead")
time.sleep(2)
fire3(c, video = True, show_final = False, q = 0.1)
