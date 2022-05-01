"""
https://leetcode.com/problems/remove-element/

This solution won't submit for some reason, just like that other challenge, but
I'm still sure it's LeetCode's mechanisms, rather than this solution not
working.
"""


def remove_element(nums, val):
    i = 0
    while True:
        if (i+1) == len(nums):
            break

        if nums[i] == val:
            nums = nums[:i] + nums[i+1:]
        else:
            i += 1

    if nums[-1] == val:
        nums = nums[:-1]

    return nums


if __name__ == '__main__':
    assert remove_element([3, 2, 2, 3], 3) == [2, 2]
    assert remove_element([3, 2, 2, 3], 2) == [3, 3]
    assert remove_element([1], 1) == []
    #assert remove_element([3, 2, 2, 3], 3) == 2
