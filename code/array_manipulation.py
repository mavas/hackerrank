"""
https://www.hackerrank.com/challenges/crush/problem

I found this explanation, which shows that my initial thinking was obvious but
incorrect, and that you have to approach the problem in a non-obvious and novel
way, using a "slope":
https://github.com/rzm5596/Array_Manipulation_HackerRank_Python

I also found this, describing my initial approach as naive:
https://www.techrbun.com/array-manipulation-hackerrank-solution/

https://sites.northwestern.edu/acids/2018/11/12/solution-hackerrank-array-manipulation/

I also found this video, with a much more visual description, and also shows
why they do B+1 instead of just B. https://www.youtube.com/watch?v=JtJKn_c9lB4
"""


def _solve_method_1(N, queries):
    """
    My first pass at this, of course, it's dumb obvious approach, but it passed
    the initial test cases on HackerRank, but I figured there would be
    performance issue test cases specifically, for bigger inputs.  And sure
    enough, there were many more that failed due to runtime.
    """
    arr = [0] * N
    largest = -1

    for query in queries:
        for i in range(query[0], query[1]+1):
            arr[i-1] = arr[i-1] + query[2]
            if arr[i-1] > largest:
                largest = arr[i-1]

    return largest


def _solve_method_2(N, queries):
    """
    This section right here uses some Pythonic optimizations, but they still
    don't cut on speed.  This at least is much faster I think, assuming each of
    these operations is atomic.
    """
    arr = [0] * N
    largest = -1

    for query in queries:
        from operator import add
        difference = abs(query[0] - (query[1]+1))
        temp_arr = [query[2]] * difference
        temp_arr_2 = arr[query[0]-1:query[1]]
        arr[query[0]-1:query[1]] = list(map(add, temp_arr_2, temp_arr))

    return max(arr)


def _solve_method_3(N, queries):
    """Me manually trying to mimic/perform/do the "slope" method."""
    arr = [0] * N

    for query in queries:
        a, b, k = query[0], query[1], query[2]
        arr[a-1] += k
        arr[b] -= k

    largest = -1
    for i in arr:
        if i > largest:
            largest = i

    return largest


def array_manipulation(N, queries):
    return _solve_method_3(N, queries)
    return _solve_method_2(N, queries)


if __name__ == '__main__':
    assert array_manipulation(10, [[1, 5, 3], [4, 8, 7], [6, 9, 1]]) == 10
    assert array_manipulation(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]]) == 200
    assert array_manipulation(5, [[1, 3, 3], [1, 5, 5]]) == 8
