# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:47:36 2019

@author: Student
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([[1, 2, 3], [2, 4, 6], [3, 6, 9], [4, 8, 12]])  
"""
x =  1   2
     3   4
"""

y = np.array([[5, 6, 7, 8], [10, 12, 14, 16]])
"""
y =   5  6
      7  8
"""

x0 = np.size(x, 0)
x1 = np.size(x, 1)
y0 = np.size(y, 0)
y1 = np.size(y, 1)

t0 = max(x0, y0)
t1 = max(x1, y1)
k0 = min(x0, y0)
k1 = min(x1, y1)

temp0 = np.zeros((t0 - k0, t1), dtype = int)
temp1 = np.zeros((t0, t1 - k1), dtype = int)

xa = x
ya = y
xb = x
yb = y

if (x0 > y0):
    ya = np.append(ya, temp0, 0)
    xb = np.delete(xb, np.s_[k0:t0], 0)

else:
    xa = np.append(xa, temp0, 0)
    yb = np.delete(yb, np.s_[k0:t0], 0)

if (x1 > y1):
    ya = np.append(ya, temp1, 1)
    xb = np.delete(xb, np.s_[k1:t1], 1)

else:
    xa = np.append(xa, temp1, 1)
    yb = np.delete(yb, np.s_[k1:t1], 1)

print (np.add(xa, ya))
print ("")
print (np.add(xb, yb))


"""
x3 = np.delete(np.delete(x, 3, 0), 2, 0)
y3 = np.delete(y, 3, 1)
print (np.add(x3, y3))
"""