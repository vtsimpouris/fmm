# -*- coding: utf-8 -*-
"""
author: Vaggelis Tsimpouris
simple 2d taylor expansion implementation
calculates the func F(x,y) using taylor expansion around a center(a,b) 
"""
from sympy import *
import numpy as np
import math

def pascal_triangle(n):
    x = [[0] * n for i in range(n)]
    for i in range(n):
        x[i][0] = 1;
    for j in range(1,n):
        for i in range(1,n):
            x[j][i] = x[j - 1][i - 1] + x[j - 1][i];
    return x
" a,b is the center of taylor expansion, be default is (0,0) "
a = 0;
b = 0;
" n is the number of taylor terms we want "
n = 3;
" x,y is the point in which f(x,y) is calculated "
x = 0.55
y = 0.33
tempx = x
tempy = y
x,y = symbols('x y')
" F is the kernel function " 
F = 1/sqrt((x-10)**2+(y-10)**2)




f = [[0] * n for i in range(n)]
f[0][0] = F

for i in range(1,n):
    for j in range(0,i):
        f[i][j] = diff(f[i-1][j],x);
    f[i][j+1] = diff(f[i-1][j],y);

p = pascal_triangle(n)
for i in range(n):
    for j in range(i):
        f[i][j] = f[i][j]*p[i][j]
        
f = lambdify( [x,y], f, "numpy")
f = f(a,b)

#calculate f(x,y)
x = tempx
y = tempy
v = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(i+1):
        v[i][j] = ((x-a)**(i-j))*((y-b)**j)
        
        
for i in range(n):
    for j in range(i+1):
        f[i][j] = f[i][j]*v[i][j]
sumf = [[0] * 1 for i in range(n)]
f = np.asarray(f)
for i in range(n):
    for j in range(i+1):
        sumf[i] += f[i][j]
    sumf[i] = sumf[i]/(math.factorial(i))
Taylor = 0
for i in range(n):
    Taylor += sumf[i]
print("Taylor calculation is = %f" % (Taylor))
answer = 1/sqrt((x-10)**2+(y-10)**2)
print("real function value is = %f" %(answer))
error = (answer - Taylor)/answer
print("relative error is = %f " % (error))


