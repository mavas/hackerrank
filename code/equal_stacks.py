"""
https://www.hackerrank.com/challenges/equal-stacks/problem

Solves the first test case, but needs to be optimized.
"""


def equal_heights(a, b, c):
    return sum(a) == sum(b) == sum(c)


def equal_stacks(a, b, c):

    while not equal_heights(a, b, c):
        f1 = sum(a)
        f2 = sum(b)
        f3 = sum(c)

        if f1 != f2 and f2 != f3 and f1 != f3:
            if f1 > f2 and f2 > f3:
                a = a[1:]
            elif f2 > f1 and f1 > f3:
                b = b[1:]
            else:
                c = c[1:]
        elif f1 == f2:
            if f2 > f3:
                a = a[1:]
                b = b[1:]
            else:
                c = c[1:]
        elif f1 == f3:
            if f2 < f3:
                a = a[1:]
                c = c[1:]
            else:
                b = b[1:]
        elif f2 == f3:
            if f1 < f2:
                b = b[1:]
                c = c[1:]
            else:
                a = a[1:]

    return sum(a)


if __name__ == '__main__':
    assert equal_stacks([1, 2, 1, 1], [1, 1, 2], [1, 1]) == 2
