"""
https://codeforces.com/gym/102069/problem/D

cat code/dima_and_array_test_1.txt | python code/dima_and_array.py
"""


import os
import fileinput
import sys


def find_mex(a):
    i = 0
    for item in a:
        if i in a:
            i += 1
            continue
        else:
            return i


def process_instruction(i, a):
    if i[0] == '?':
        left_index = i[1] - 1
        right_index = i[2]
        new_a = a[left_index:right_index]
        print(find_mex(new_a))
        return a
    elif i[0] == '!':
        a[i[1]-1] = i[2]
        return a
    else:
        raise Exception


def main():
    with fileinput.input() as fh:
        N, Q = fh.readline().strip().split()
        N = int(N)
        Q = int(Q)
        a = fh.readline().strip().split()
        a = [int(x) for x in a]

        while True:
            instruction = fh.readline().strip().split()
            if len(instruction) > 0:
                instruction[1] = int(instruction[1])
                instruction[2] = int(instruction[2])
                a = process_instruction(instruction, a)
            else:
                break


if __name__ == '__main__':
    main()
    #case_1 = [13, 11, 11, 11, 13, 11]
    #assert compute_minimum(1, case_1) == "Case #1: 82"
