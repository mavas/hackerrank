"""
https://www.hackerrank.com/challenges/one-week-preparation-kit-lonely-integer/problem
"""


def _solve_method_2(a):
    """Use a dictionary."""
    d = dict()
    for item in a:
        if not item in d:
            d[item] = 1
        else:
            d[item] += 1

    for k, v in d.items():
        if v == 1:
            return k


def _solve_method_1(a):
    """First sort them, and then count by two's, until a 'problem' is found."""
    a = sorted(a)
    found_it = a[0]


def lonely_integer(a):
    return _solve_method_2(a)


if __name__ == '__main__':
    assert lonely_integer([1, 2, 3, 4, 3, 2, 1]) == 4
