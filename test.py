import numpy as np
from GEPP import *
#import GEPP 

print("Create matrix")
A = np.array([  [1,2,3],
                [3,4,5],
                [3,2,1]])
y = np.array([  [1],
                [3],
                [4]])
Gause = GEPP(np.copy(A), np.copy(y), doPricing=False)
print(Gause.x)
print(Gause.A)
print(Gause.b)
