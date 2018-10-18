# -*- coding: utf-8 -*-
"""
author: Vaggelis Tsimpouris
simple 3d taylor expansion implementation
calculates the func F(x,y,z) using taylor expansion around a center(a,b,c) 
"""
from sympy import *
import numpy as np
import math
from scipy.special import factorial as fact

def pascal_pyramid(n):
    p = np.zeros((n+1,n+1))
    p = [[(fact(n)/(fact(n-i-j)*fact(i)*fact(j))) if j < n+1-i else 0 for j in range(n+1)]for i in range(n+1)]
    return p
    
" cx,cy,cz is the center of taylor expansion, be default is (0,0,0) "
cx = 0;
cy = 0;
cz = 0;
" n is the number of taylor terms we want "
n = 3;
" x,y,z is the point in which f(a,b,c) is calculated "
a = 0.55
b = 0.33
c = 0.22
x,y,z = symbols('x y z')
" F is the kernel function " 
F = 1/sqrt((x-10)**2+(y-10)**2+(z-10)**2)
f = [[[0 for k in range(n+1)] for j in range(n+1)] for i in range(n+1)]
f[0][0][0] = F
for m in range(n):
    for i in range(m+2):
        for j in range(m+2-i):
            f[m+1][i][j] = diff(F,x,m-i-j+1);
            f[m+1][i][j] = diff(f[m+1][i][j],y,i);
            f[m+1][i][j] = diff(f[m+1][i][j],z,j);
f = lambdify( [x,y,z], f, "numpy")
f = f(cx,cy,cz)
'matlab matrix f(x,y,z) is in python f(z,x,y)'           