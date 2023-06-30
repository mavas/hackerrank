"""
https://codeforces.com/gym/104022/problem/I


cat test_case_1.txt

2
6
13 11 11 11 13 11
6
13 11 11 11 13 11
"""


import os
import fileinput
import sys
import math


def compute_minimum(test_case_number, test_case):
    return result


def main():
    input_file = os.path.abspath('./test_case_1.txt')

    with fileinput.input() as fh:
        lines = fh.readline().strip()
        n_cases = int(lines[0])
        test_case_number = 0

        while True:
            has_something = fh.readline().strip()
            if len(has_something) > 0:
                test_case_number += 1
                n_tournaments = int(has_something)
                tournaments = [int(x) for x in fh.readline().split()]
                compute_minimum(test_case_number, tournaments)
            else:
                break


if __name__ == '__main__':
    main()
    #case_1 = [13, 11, 11, 11, 13, 11]
    #assert compute_minimum(1, case_1) == "Case #1: 82"
