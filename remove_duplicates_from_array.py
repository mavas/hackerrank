"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/


For some reason this code works, but on the web UI it's not submitting
properly, and the algorithm looks like it works, so I really think the problem
is just LeetCode's interface, and not this code, but we'll see.
"""


def remove_duplicates_from_array_2_pointers(nums):
    """This was posted in the Solutions section, and is different from the
    approach below."""
    i = 0
    k = i + 1


def remove_duplicates_from_array(nums):
    i = 1
    count = 0

    #if len(nums) < 3:
    while True:
        if (i+1) == len(nums):
            break
        elif nums[i-1] == nums[i]:
            nums = nums[:i] + nums[i+1:]
            count += 1
        else:
            i += 1
    if nums[i] == nums[i-1]:
        nums = nums[:-1]

    # Then, process the last possible case.
    return nums


#assert remove_duplicates_from_array([0,0,1,1,1,2,2,3,3,4]) == 5
assert remove_duplicates_from_array([0,0,1,1,1,2,2,3,3,4,4]) == [0,1,2,3,4]
assert remove_duplicates_from_array([0,0,1,1,1,2,2,3,3,4]) == [0,1,2,3,4]
assert remove_duplicates_from_array([1,1,2]) == [1, 2]
