function [ p ] = pascal_pyramid( n )
%%author: evangelos tsimpouris
%n is the layer of the pascal _ pyramid
p = zeros(n+1,n+1)
    for i = 1:n+1
        for j = 1:n+1 -i +1
            p(i,j) = factorial(n) / (factorial(n-i-j+2)*factorial(i-1)*factorial(j-1));
        end
    end


end

