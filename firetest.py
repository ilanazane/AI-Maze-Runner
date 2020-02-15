from methods import *
from fire1 import fire1
from fire2 import fire2

#make copies of the same maze to be run by each algorithm
a = firegrid(10, 0.2)
b = np.copy(a)

fire1(a, video = True, show_final = True, q = 0.1)
fire2(b, video = True, show_final = True, q = 0.1)
