"""
https://codeforces.com/gym/102069/problem/D

cat code/dima_and_array_test_1.txt | python code/dima_and_array.py
"""


import os
import fileinput
import sys


def main():
    with fileinput.input() as fh:
        N, Q = fh.readline().strip().split()
        N = int(N)
        Q = int(Q)
        print(N, Q)
        a = fh.readline().strip().split()
        a = [int(x) for x in a]
        print(a)

        while True:
            instruction = fh.readline().strip()
            if len(instruction) > 0:
                print(instruction)
            else:
                break


if __name__ == '__main__':
    main()
    #case_1 = [13, 11, 11, 11, 13, 11]
    #assert compute_minimum(1, case_1) == "Case #1: 82"
