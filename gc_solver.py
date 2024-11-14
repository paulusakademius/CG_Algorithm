import numpy as np 

matrix = np.array([[6,2,3],[2,7,4],[3,4,8]])

x_0 = np.array([1,1,1])

b =  np.array([1,2,3])

r_0 = b - matrix.dot(x_0)


