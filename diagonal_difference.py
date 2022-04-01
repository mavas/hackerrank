"""
https://www.hackerrank.com/challenges/one-week-preparation-kit-diagonal-difference/problem
"""


def _solve_method_1(a):
    """Literally did this first and was surprised when it didn't work on any
    other test case, and then found out about the problem inputs."""
    first_d = a[0][0] + a[1][1] + a[2][2]
    second_d = a[0][2] + a[1][1] + a[2][0]
    return abs(first_d - second_d)


def _solve_method_2(a):
    """More generalized to any same-sided square."""
    N = len(a)

    i = 0  # row
    j = 0  # column
    first_d = 0
    while i < N and j < N:
        first_d += a[i][j]
        i += 1
        j += 1

    j = N - 1
    i = 0
    second_d = 0
    while i < N and j >= 0:
        second_d += a[i][j]
        i += 1
        j -= 1

    return abs(first_d - second_d)


def diagonal_difference(a):
    return _solve_method_2(a)


if __name__ == '__main__':
    assert diagonal_difference([[1, 2, 3], [4, 5, 6], [9, 8, 9]]) == 2
