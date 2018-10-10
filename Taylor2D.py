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
    x = np.zeros((n,n))
    for i in range(n):
        x[i,0] = 1;
    for j in range(1,n):
        for i in range(1,n):
            x[j,i] = x[j - 1,i - 1] + x[j - 1,i];
    return x

" cx,cy is the center of taylor expansion, be default is (0,0) "
cx = 0;
cy = 0;
" n is the number of taylor terms we want "
n = 10;
" x,y is the point in which f(a,b) is calculated "
a = 0.55
b = 0.33
x,y = symbols('x y')
" F is the kernel function " 
F = 1/sqrt((x-10)**2+(y-10)**2)


f = [[0] * n for i in range(n)]
f[0][0] = F

for i in range(1,n):
    for j in range(0,i):
        f[i][j] = diff(f[i-1][j],x);
    f[i][j+1] = diff(f[i-1][j],y);
f = lambdify( [x,y], f, "numpy")
f = f(cx,cy)
p = pascal_triangle(n)
f=np.multiply(f,p)
        
#calculate f(x,y)
v = np.zeros((n,n))
for i in range(n):
    for j in range(i+1):
        v[i,j] = ((a-cx)**(i-j))*((b-cy)**j)               
f=np.multiply(f,v)

sumf = np.zeros(n)
for i in range(n):
    sumf[i] = sum(f[i])
    sumf[i] = sumf[i]/(math.factorial(i))
Taylor = sum(sumf)
print("Taylor calculation is = %.20f" % (Taylor))
answer = 1/sqrt((a-10)**2+(b-10)**2)
print("real function value is = %.20f" %(answer))
error = math.fabs((answer - Taylor)/answer)
print("relative error is = %.20f " % (error))
print("log10 of error is = %.5f " % (math.log10(error)))


