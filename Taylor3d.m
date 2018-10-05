clear all;
close all;
a = 0;
b = 0;
c = 0;
n = 10;

syms x y z;
syms F(x,y,z);
F(x,y) = 1/sqrt((x-10)^2+(y-10)^2+(z-10)^2);
f = sym('f',[n n n]);
%for i = 1:m
%    f(i) = sym('f',[i+1 i+1]);
%end
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
f = subs(f);
for m = 1:n
    p = pascal_pyramid(m);
    for i = 1:m+1
        for j = 1:m+1 -i +1
            f(i,j,m+1) = p(i,j)*f(i,j,m+1);
        end
    end
end
(((n+1)*(n+1) - (n+1) )  /2)