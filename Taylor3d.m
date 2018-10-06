clear all;
close all;
a = 0;
b = 0;
c = 0;
n = 4;

syms x y z;
syms F(x,y,z);
F(x,y) = 1/sqrt((x-10)^2+(y-10)^2+(z-10)^2);
f = sym('f',[n n n]);
%for i = 1:m
%    f(i) = sym('f',[i+1 i+1]);
%end
%number of terms for each taylor layer = (((n+1)*(n+1) - (n+1) )  /2)
f(1,1,1) = F;
for m = 1:n
    for i = 1:m+1
        for j = 1:m+1 -i +1
            f(i,j,m+1) = diff(F,x,m-i-j+2);
            f(i,j,m+1) = diff(f(i,j,m+1),y,i-1);
            f(i,j,m+1) = diff(f(i,j,m+1),z,j-1);
        end
    end
end
x = a;
y = b;
z = c;
f = vpa(subs(f));
for m = 1:n
    p = pascal_pyramid(m);
    for i = 1:m+1
        for j = 1:m+1 -i +1
            f(i,j,m+1) = p(i,j)*f(i,j,m+1);
        end
    end
end
syms x y z;
v = sym('v', [n n n]);
v(1,1,1) = 1;
for m = 1:n
    for i = 1:m+1
        for j = 1:m+1 -i +1
            v(i,j,m+1) = ((x-a)^(m-i-j+2)) * ((y-b)^(i-1)) * ((z-c)^(j-1));
        end
    end
end
%% calculate f(x,y,z)
x = vpa(1);
y = vpa(1);
z = vpa(1);
v = vpa(subs(v));
sumf = vpa(zeros(n+1,1));
sumf(1) = f(1,1,1)*v(1,1,1); 
for m = 1:n
    for i = 1:m+1
        for j = 1:m+1 -i +1
            sumf(m+1) = sumf(m+1) + f(i,j,m+1)*v(i,j,m+1);
        end
    end
    sumf(m+1) = sumf(m+1)/factorial(m);
end
answer = 1/sqrt((x-10)^2+(y-10)^2+(z-10)^2)
Taylor = vpa((sum(sumf)))
error = vpa(abs((answer - Taylor)/answer))






