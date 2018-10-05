close all;
clear all;
%a,b is center of expansion
a = 1;
b = 1;
m = 10;

syms x y;
syms F(x,y);
F(x,y) = 1/sqrt((x-1000)^2+(y-1000)^2);
f = sym('f',[m m]);
f(1,1) = F;

for i = 2:m
    for j = 1:i-1
        f(i,j) = diff(f(i-1,j),x,1);
    end
    f(i,j+1) = diff(f(i-1,j),y,1);
end
pt = pascal_triangle(m);
%center is (a,b) = (1,1)
x = a;
y = b;
f = subs(f);
for i = 1:m
    for j = 1:i
        f(i,j) = pt(i,j)*f(i,j);
    end
end
syms x y;
f2 = sym('f2',[m m]);
for i =1:m
    for j =1:i
        f2(i,j) = ((x-a)^(i-j))*((y-b)^(j-1));
    end
end
        
for i = 1:m
    for j = 1:i
        f(i,j) = f(i,j)*f2(i,j);
    end
end

%% calculate f(x,y)
x = 1.05;
y = 1.05;
f = subs(f);
ff = zeros(m,1);

for i = 1:m
    for j = 1:i
        ff(i) = ff(i) + f(i,j);
    end
end
for i = 1:m
    ff(i) = ff(i)/factorial(i);
end
answer = 1/sqrt((x-1000)^2+(y-1000)^2)
Taylor = sum(ff)
error = abs((answer - Taylor)/answer)
    
    
    
