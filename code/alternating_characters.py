"""
https://www.hackerrank.com/challenges/alternating-characters/problem
"""


def alternating_characters(s):
    """
    Returns the minimum number of required deletions to make the string have no
    repeated characters.

    Implemented this first try, passing all test cases, earning 20 points,
    January 17, 2022.
    """
    current_character = s[0]
    delete_counter = 0
    
    for character in s[1:]:
        if character == current_character:
            delete_counter += 1
        else:
            current_character = character
    
    return delete_counter


if __name__ == '__main__':
    # One of the first 2 A's, and one of the 2nd pair of A's.  So, 2 characters.
    assert alternating_characters('AABAAB') == 2
    assert alternating_characters('BBBBB') == 4
    assert alternating_characters('ABABABABABAB') == 0
