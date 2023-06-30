"""
https://codeforces.com/gym/102441/problem/B

3
1234 2 21 43
12534 2 21 43
42 1 42

14 23
-1
42
"""


import fileinput


def compute(s, n, a):
    s_changed = []
    [s_changed.append(int(i)) for i in s]
    s = sorted(s_changed)
    s.reverse()
    print(s, a)

    # First see if it's possible, only given the number of digits in 's',
    # compared with the length of any of the upper bounds numbers.
    for number in a:
        if len(s) > len(a):
            return "-1"

    print(type(a))
    print(a)


def main():
    with fileinput.input() as fh:
        N = int(fh.readline().strip())

        for line in range(N):
            test_case = fh.readline().strip()
            s, n, a = test_case.split(' ', 2)
            n = int(n)
            a = ' '.join(a.split())
            compute(s, n, a)


if __name__ == '__main__':
    #main()
    s = "12534"
    n = "2"
    a = [21, 43]
    assert compute(s, n, a) == "-1"

    s = "1234"
    n = "2"
    a = "21 43"
    assert compute(s, n, a) == "14 23"
