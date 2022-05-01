# https://www.hackerrank.com/challenges/bash-tutorials---arithmetic-operations/problem
read var
printf "%.3f" `echo $var | bc -l`
