"""
Recursion and Backtracking:
https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem
"""


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    TWO = 2
    assert fibonacci(TWO) == fibonacci(TWO - 1) + fibonacci(TWO - 2) == 1
    THREE = 3
    assert fibonacci(THREE) == fibonacci(THREE - 1) + fibonacci(THREE - 2) == 2
