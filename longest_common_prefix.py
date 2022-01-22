"""
https://leetcode.com/problems/longest-common-prefix/
"""


def longest_common_prefix(strs):
    """Submitted this and it passed all test cases January 18, 2022."""
    o = ""

    # Find/compute the length of the shortest item in the list.
    shortest_seen_so_far = 201
    for item in strs:
        if len(item) < shortest_seen_so_far:
            shortest_seen_so_far = len(item)

    # Loop from i=0 until i==length_of_shortest_item.  On each iteration, we're
    # comparing the ith character in all of the items in the list, and seeing
    # if they are all equal to each other.  If so, that means that this is part
    # of a valid sequence; if they don't all equal each other, we can end the
    # loop and return our answer.
    i = 0
    while i < shortest_seen_so_far:
        character = strs[0][i]
        for item_character in strs[1:]:
            if item_character[i] != character:
                return o
        o += character
        i += 1

    return o


if __name__ == '__main__':
    assert longest_common_prefix(['flower', 'flow', 'flight']) == 'fl'
    assert longest_common_prefix(["dog","racecar","car"]) == ""
