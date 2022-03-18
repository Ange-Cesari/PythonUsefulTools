from itertools import product
import numpy as np
l=[]
for i in product([0,1], repeat=8):
    l.append(list(i))
print(l)
