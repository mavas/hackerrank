"""
I think this one may be:
https://www.hackerrank.com/challenges/minimum-swaps-2/problem

I'm not sure how I completed this online, because I passed it, but the solution
was mostly here locally in this repository, but these test cases don't work.
Maybe I'll work on it later.
"""


def all_done(arr):
    for item in arr:
        if not isinstance(item, int):
            return False
    return True


# Iteratively, using outer and inner indices.
def _method_2(data_arr):
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

def _compute_2_swap_positions_2(data_arr):
    """Selects to disjoint positions randomly."""
    import random
    while True:
        first_one = random.randrange(len(data_arr))
        second_one = random.randrange(len(data_arr))
        if first_one == second_one: continue
        if not isinstance(data_arr[first_one], int):
            if not isinstance(data_arr[second_one], int):
                return (first_one, second_one)

def _update_entries(data_arr, first_one, second_one):
    """Replaces 2 entries in the array, and returns the modified array."""
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

def _augment_array(arr):
    data_arr = []
    for index, item in enumerate(arr):
        intended_index = item - 1
        if index != intended_index:
            difference = abs(intended_index - index)
            data_arr.append((item, difference))
        else:
            data_arr.append(item)
    return data_arr


def minimumSwaps(arr):
    """Return the minimum number of swaps to sort the array."""
    data_arr = _augment_array(arr)

    count = 0
    while not all_done(data_arr):
        (first_one, second_one) = _compute_2_swap_positions_2(data_arr)
        data_arr = _update_entries(data_arr, first_one, second_one)
        count += 1

    return count


if __name__ == '__main__':
    assert minimumSwaps([7, 1, 3, 2, 4, 5, 6]) == 5
