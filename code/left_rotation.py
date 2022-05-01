"""
https://www.hackerrank.com/challenges/ctci-array-left-rotation
"""


def left_rotate_2(a, d):
    """Naive rotation."""


def left_rotate(a, d):
    """Python array slicing."""
    if d == 0: return a
    first = a[:d]
    second = a[d:]
    return second + first


if __name__ == '__main__':
    assert left_rotate([1, 2], 1) == [2, 1]
    assert left_rotate([1, 2], 0) == [1, 2]
    assert left_rotate([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]
    assert left_rotate([1, 2, 3, 4, 5], 4) == [5, 1, 2, 3, 4]
