"""
https://www.hackerrank.com/challenges/icecream-parlor/problem
"""


def icecreamParlor(m, arr):
    decorated_arr = []
    for index, item in enumerate(arr):
        decorated_arr.append((item, index))

    import itertools
    for item in itertools.permutations(decorated_arr, 2):
        pass
    for item in itertools.combinations(decorated_arr, 2):
        pass
    for i in decorated_arr:
        for j in decorated_arr:
            if (i[0] + j[1]) == m and i[1] != j[1]:
                return [i[1] + 1, j[1] + 1]


def icecreamParlor(m, arr):
    """
    This involves using a sorted array, and binary search.  This method works,
    but I still have yet to truely understand how it works; more thinking about
    it needs to be done.

    https://github.com/ashikrafi/Ice-Cream-Parlor-Binary-Search-Python-HackerRank/

    :param m: How many dollars you have.
    :param arr: The list of prices of ice cream.
    """
    def _binary_search(sequence, value):
        lo = 0
        hi = len(sequence) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if sequence[mid] < value:
                lo = mid + 1
            elif value < sequence[mid]:
                hi = mid - 1
            else:
                return mid
        return -1

    sorted_arr = sorted(arr)
    item_index = []

    for x in range(len(arr)):
        complement = m - arr[x]
        index = _binary_search(sorted_arr, complement)

        if ((arr[x] + sorted_arr[index]) == m):
            item_index.append(x+1)
            index_val = arr.index(sorted_arr[index])

            if (arr[x] == sorted_arr[index]):
                index_val += 1

            item_index.append(index_val +1)
            break

    return (item_index)


def icecreamParlor3(m, arr):
    """
    Uses randomness to find the 2 indeces

    This won't work on competitive programming submissions that test with large
    inputs.  It's not optimal, but works on small inputs.
    """
    import random
    N = len(arr)
    while True:
        first_one = random.randrange(N)
        second_one = random.randrange(N)
        if first_one == second_one:
            continue
        if (arr[first_one] + arr[second_one]) == m:
            if first_one > second_one:
                temp = second_one
                second_one = first_one
                first_one = temp
            return [first_one+1, second_one+1]


def icecreamParlor2(m, arr):
    """
    This solution involves sorting the numbers first.  Select one from the
    front, and compare them to all of the ones counting back from the back.
    """
    o = None
    sorted_arr = sorted(arr)
    i = 0
    k = len(sorted_arr-1)
    return (o[0]+1, o[1]+1)


def icecreamParlor4(m, arr):
    """I forgot about Python's nested for loops - on the SAME array - and how
    that's actually -possible-, and it makes things so much simplier.

    It turns out, that this works, but only for small inputs."""
    # Augment the array of data, so that it not only includes the item, but
    # also the item's index into the array.
    decorated_arr = []
    for index, item in enumerate(arr):
        decorated_arr.append((item, index))

    # Iterate each combination of index, and see if conditions are met with
    # them.  There are 2 things we care about: both amounts equal to m, and
    # they both aren't the same item.
    for i in decorated_arr:
        for j in decorated_arr:
            if (i[0] + j[1]) == m and i[1] != j[1]:
                return [i[1] + 1, j[1] + 1]


if __name__ == '__main__':
    # Items 1 and 4 sum to equal 6.
    #assert icecreamParlor(6, [1, 3, 4, 5, 6]) == (1, 4)
    print(icecreamParlor(6, [1, 3, 4, 5, 6]))

    # Items 1 and 4 sum to equal 4.
    #assert icecreamParlor(4, [1, 4, 5, 3, 2]) == (1, 4)
    print(icecreamParlor(4, [1, 4, 5, 3, 2]))
    assert icecreamParlor3(4, [1, 4, 5, 3, 2]) == [1, 4]
    assert icecreamParlor4(4, [1, 4, 5, 3, 2]) == [1, 4]

    # Items 1 and 1 sum to equal 4.
    assert icecreamParlor(4, [2, 2, 4, 3]) == [1, 2]
    assert icecreamParlor3(4, [2, 2, 4, 3]) == [1, 2]
