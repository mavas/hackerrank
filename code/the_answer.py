"""
https://codeforces.com/gym/104022/problem/I


cat test_case_1.txt

3
3 3 3 97
7 3 2 1901
6 12 3 100

1
1761
98
"""


import fileinput
import math
import os
import sys


def main_stdin():
    """
    Compute the answer, reading test cases from standard input.
    """

    with fileinput.input() as fh:
        lines = fh.readline().strip()
        n_cases = int(lines[0])

        while True:
            has_something = fh.readline().strip()
            if len(has_something) > 0:
                n_tournaments = int(has_something)
                tournaments = [int(x) for x in fh.readline().split()]
                compute_the_answer(tournaments)
            else:
                break


def fib(n):
    """
    Computes the Fibonacci sequence.
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n >= 3:
        return fib(n-1) + fib(n-2)


def compute_the_answer(x, y, a, m):
    """
    fib(6) = fib(5) + fib(4) = fib(5) + [fib(3) + fib(2)]
    """
    f_x = fib(x)
    print("f_x: %s" % f_x)
    f_y = fib(y)
    print("f_y: %s" % f_y)
    u = a**f_x - 1
    print("u: %s" % u)
    v = a**f_y - 1
    print("v: %s" % v)
    ratio = math.lcm(u, v) / math.gcd(u, v)
    result = ratio % m
    result2 = math.remainder(ratio, m)
    print(ratio, result, result2)
    return result


if __name__ == '__main__':
    #main_stdin()

    assert compute_the_answer(3, 3, 3, 97) == 1
    print()
    assert compute_the_answer(7, 3, 2, 1901) == 1761
    print()
    assert compute_the_answer(6, 12, 3, 100) == 98
