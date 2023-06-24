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


def main():
    with fileinput.input() as fh:
        N = fh.readline().strip()
        print(N)


if __name__ == '__main__':
    main()
