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
    print(s, n)
    print(a)


def main():
    with fileinput.input() as fh:
        N = int(fh.readline().strip())

        for line in range(N):
            test_case = fh.readline().strip()
            s, n, a = test_case.split(' ', 2)
            compute(s, n, a)


if __name__ == '__main__':
    main()
