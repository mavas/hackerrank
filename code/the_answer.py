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


def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def compute_the_answer(x, y, a, m):
    f_x = fib(x)
    f_y = fib(y)
    u = a**f_x - 1
    v = a**f_y - 1
    return (math.lcm(u, v) / math.gcd(u, v)) % m


def main_stdin():
    """
    Compute the answer, reading test cases from standard input.
    """

    with fileinput.input() as fh:
        lines = fh.readline().strip()
        n_cases = int(lines[0])
        test_case_number = 0

        while True:
            has_something = fh.readline().strip()
            if len(has_something) > 0:
                test_case_number += 1
                n_tournaments = int(has_something)
                tournaments = [int(x) for x in fh.readline().split()]
                compute_minimum(test_case_number, tournaments)
            else:
                break


if __name__ == '__main__':
    #main_stdin()

    case_1 = [3, 3, 3, 97]
    assert compute_the_answer(3, 3, 3, 97) == 1
    assert compute_the_answer(7, 3, 2, 1901) == 1761
    assert compute_the_answer(6, 12, 3, 100) == 98
