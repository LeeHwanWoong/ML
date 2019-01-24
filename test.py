import numpy as np
from perceptron import pcn

input = np.array([[0,0],[0,1],[1,0],[1,1]])
target = np.array([[0],[1],[1],[1]])
p = pcn(input,target)
p.train(0.25,10)
