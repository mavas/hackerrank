"""
I think this one may be:
https://www.hackerrank.com/challenges/minimum-swaps-2/problem

First try thoughts (_solve_method_1):
    I'm not sure how I completed this online, because I passed it, but the solution
    was mostly here locally in this repository, but these test cases don't work.
    Maybe I'll work on it later.

Coming back:
    What's interesting is that the swap order in the HackerRank algorithm, for
    this test case, is different from the swap order in _solve_method_3, but
    they both are the "minimum"; that means that there's not necessarily a
    unique minimum:

    HackerRank demonstration:
        i   arr                     swap (indices)
        0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
        1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
        2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
        3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
        4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
        5   [1, 2, 3, 4, 5, 6, 7]

    The algorithm below (_solve_method_3):
          1 before: [7, 1, 3, 2, 4, 5, 6]
            after : [6, 1, 3, 2, 4, 5, 7]
          2 before: [6, 1, 3, 2, 4, 5, 7]
            after : [5, 1, 3, 2, 4, 6, 7]
          3 before: [5, 1, 3, 2, 4, 6, 7]
            after : [4, 1, 3, 2, 5, 6, 7]
          4 before: [4, 1, 3, 2, 5, 6, 7]
            after : [2, 1, 3, 4, 5, 6, 7]
          5 before: [2, 1, 3, 4, 5, 6, 7]
            after : [1, 2, 3, 4, 5, 6, 7]

    I think I understand how my original thinking was different from this
    solution. I was trying to incorporate BOTH swap positions, and trying to
    make an intelligent swap incorporating both of them somehow; that other
    solution simply takes the current value at the current position, and swaps
    whatever value is in its correct position, with the current position.  That
    method involves only making an intelligent/wise choice about 1 position,
    but I thought that was too naive I think, or maybe I was overthinking, but
    it was actually good/correct.

    Both diagrams above make DIFFERENT swaps, but they both total to a number
    of 5, and my original thinking was more in line with the first example much
    rather than the second example.  You see that the second example almost
    works backwards from the end, and the first one is rather sporadic.  I
    tried to find some pattern in that sporadicness.  I mean, really think
    about it: how did those folks over at HackerRank come up with those swaps
    in the first place?  What algorithm produces those swaps?
"""


def all_done(arr):
    """I think this is specific to the augmented data array;"""
    for item in arr:
        if not isinstance(item, int):
            return False
    return True


def _solve_method_2(data_arr):
    """
    Iteratively, using outer and inner indices.

    This was some other attempted method/path of thinking towards a solution
    that I didn't finish.
    """
    # It wasn't worth the attention to detail.
    while not all_done(data_arr):
        i = 0
        while i <= len(data_arr) - 2:
            k = i +  1
            while k <= len(data_arr) - 1:
                pass


def _compute_2_swap_positions_1(data_arr):
    """Iterates twice to discover 2 highest numbers."""
    highest_distance_so_far = (0, -1)
    second_highest_distance_so_far = (0, -1)
    for index, item in enumerate(data_arr):
        if isinstance(item, tuple):
            distance = item[1]
            if distance > highest_distance_so_far[1]:
                highest_distance_so_far = (index, distance)

    for index, item in enumerate(data_arr):
        if index != highest_distance_so_far[0]:
            if isinstance(item, tuple):
                distance = item[1]
                if distance > second_highest_distance_so_far[1]:
                    second_highest_distance_so_far = (index, distance)
    print(highest_distance_so_far, second_highest_distance_so_far)
    return (highest_distance_so_far, second_highest_distance_so_far)


def _augment_array(arr):
    new_arr = []
    for index, item in enumerate(arr):
        intended_index = item - 1
        if index != intended_index:
            difference = abs(intended_index - index)
            new_arr.append((item, difference))
        else:
            new_arr.append(item)
    return new_arr

def _compute_2_swap_positions_2(data_arr):
    """Selects two disjoint positions randomly."""
    import random
    while True:
        first_one = random.randrange(len(data_arr))
        second_one = random.randrange(len(data_arr))
        if first_one == second_one: continue
        if not isinstance(data_arr[first_one], int):
            if not isinstance(data_arr[second_one], int):
                return (first_one, second_one)

def _update_entries(data_arr, first_one, second_one):
    """
    Replaces 2 entries in the array, and returns the modified array.

    This only operates on arrays returned by the likes of _augment_array().
    """
    temp1 = data_arr[first_one]
    temp2 = data_arr[second_one]

    intended_index = temp2[0] - 1
    difference = abs(intended_index - first_one)
    if difference == 0:
        data_arr[first_one] = temp2[0]
    else:
        data_arr[first_one] = (temp2[0],) + (difference,)

    intended_index = temp1[0] - 1
    difference = abs(intended_index - second_one)
    if difference == 0:
        data_arr[second_one] = temp1[0]
    else:
        data_arr[second_one] = (temp1[0],) + (difference,)

    return data_arr

def _solve_method_1(arr):
    """This method involves using Python's random module, which is not good.
    If you run this Python file, using this method, the test cases listed below
    usually fail, but occasionally all of them will pass."""

    data_arr = _augment_array(arr)

    count = 0
    while not all_done(data_arr):
        (first_one, second_one) = _compute_2_swap_positions_2(data_arr)
        data_arr = _update_entries(data_arr, first_one, second_one)
        count += 1

    return count


def _solve_method_3(arr):
    """
    https://github.com/JaredLGillespie/HackerRank/blob/master/Python/minimum-swaps-2.py

    Couldn't really figure it out via my method, but I found this solution that
    was very small and I understand.

    One thing I did was factor out a portion of it into a function call, for
    easier understanding.  A lot of times, of course, in programming, one can
    pack a lot of information in one line of code, but it's good to factor that
    out sometimes.
    """

    def _swap_2_elements(arr, first_index, second_index):
        """
        Swaps 2 positions of the array.

        This function is different from my `update_entries` function above,
        only in that my function operates on an augmented array, rather than
        a bare array.
        """
        temp = arr[first_index]
        arr[first_index] = arr[second_index]
        arr[second_index] = temp
        return arr

    n = len(arr)
    swaps = 0
    for i in range(0, n - 1):
        while arr[i] != i + 1:
            first_index = arr[i] - 1
            second_index = i
            arr = _swap_2_elements(arr, first_index, second_index)
            swaps += 1

    return swaps


def minimumSwaps(arr):
    """Return the minimum number of swaps to sort the array."""
    return _solve_method_3(arr)
    return _solve_method_1(arr)


if __name__ == '__main__':
    assert minimumSwaps([7, 1, 3, 2, 4, 5, 6]) == 5
    assert minimumSwaps([4, 3, 1, 2]) == 3
    assert minimumSwaps([2, 3, 4, 1, 5]) == 3
    assert minimumSwaps([1, 3, 5, 2, 4, 6, 7]) == 3
