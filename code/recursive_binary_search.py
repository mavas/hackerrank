"""
Me manually implementing binary search via recursion, first try.  No references
(not looking anything up - just using pdb and figuring it out).

January 8, 2022
"""


def binary_search_iterative(sequence, value):
    """Will continue to work on later (so, this function currently doesn't
    work."""
    low = 0
    high = len(sequence) - 1

    while low != high:
        mid = low + (high - low) // 2

        #if value


def binary_search(sequence, value, low, high):
    """Implements binary search, recursively.  It operates on smaller and
    smaller sections of the given array."""
    mid = low + (high - low) // 2

    if low == mid and mid == high:
        if sequence[mid] != value:
             return -1

    if value < sequence[mid]:
        return binary_search(sequence, value, low, mid-1)
    elif value > sequence[mid]:
        return binary_search(sequence, value, mid+1, high)
    else:
        return mid


def driver(sequence, value):
    sequence = sorted(sequence)
    low = 0
    high = len(sequence) - 1
    return binary_search(sequence, value, low, high)


if __name__ == '__main__':
    data = [0, 1, 1, 2, 3, 6, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    assert driver(data, 60) == -1
    assert driver(data, 6) == 5
    assert driver(data, 21) == 8
    assert driver(data, 3) == 4
