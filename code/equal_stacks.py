"""
https://www.hackerrank.com/challenges/equal-stacks/problem

Solves the first test case, but needs to be optimized.
"""


def equal_heights(a, b, c):
    return sum(a) == sum(b) == sum(c)


def equal_stacks(a, b, c):
    f1 = sum(a)
    f2 = sum(b)
    f3 = sum(c)

    while not f1 == f2 == f3:

        if f1 != f2 and f2 != f3 and f1 != f3:
            if f1 > f2 and f2 > f3:
                a = a[1:]
                f1 = sum(a)
            elif f2 > f1 and f1 > f3:
                b = b[1:]
                f2 = sum(b)
            else:
                c = c[1:]
                f3 = sum(c)

        elif f1 == f2:
            if f2 > f3:
                a = a[1:]
                f1 = sum(a)
                b = b[1:]
                f2 = sum(b)
            else:
                c = c[1:]
                f3 = sum(c)

        elif f1 == f3:
            if f2 < f3:
                a = a[1:]
                f1 = sum(a)
                c = c[1:]
                f3 = sum(c)
            else:
                b = b[1:]
                f2 = sum(b)

        elif f2 == f3:
            if f1 < f2:
                b = b[1:]
                f2 = sum(b)
                c = c[1:]
                f3 = sum(c)
            else:
                a = a[1:]
                f1 = sum(a)

    return f1


if __name__ == '__main__':
    assert equal_stacks([1, 2, 1, 1], [1, 1, 2], [1, 1]) == 2
    assert equal_stacks([3, 2, 1, 1, 1], [4, 3, 2], [1, 1, 4, 1]) == 5
