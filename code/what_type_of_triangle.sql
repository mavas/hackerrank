/*
 * https://www.hackerrank.com/challenges/what-type-of-triangle/problem
 *
 * MySQL
 * */
select
case
    when (a+b<=c) or (a+c<=b) or (b+c<=a) then 'Not A Triangle'
    when (a = b and b = c) then 'Equilateral'
    when (a = b and b != c) or (a = c and c != b) or (b = c and c != a) then 'Isosceles'
    when (a != b and b != c) then 'Scalene'
end
from triangles;
