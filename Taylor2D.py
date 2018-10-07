# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from sympy import *
import numpy as np

a = 0;
b = 0;
n = 3;
x,y = symbols('x y')

F = 1/sqrt((x-10)**2+(y-10)**2)

f = [[0] * n for i in range(n)]
f[0][0] = F

for i in range(1,n):
    for j in range(0,i):
        f[i][j] = diff(f[i-1][j],x);
    f[i][j+1] = diff(f[i-1][j],y);
f = lambdify( [x,y], f, "numpy") 
print(f(a,b))


def pascal_triangle(n):
    x = [[0] * n for i in range(n)]
    for i in range(n):
        x[i][0] = 1;
    for j in range(1,n):
        for i in range(1,n):
            x[j][i] = x[j - 1][i - 1] + x[j - 1][i];
    return x