function [ x ] = pascal_triangle( n )
  x = eye(n);
  x(:, 1) = 1;
  for j=3:n
    for i = 2 : n - 1
      x(j, i) = x(j - 1, i - 1) + x(j - 1, i);
    end
  end

end

