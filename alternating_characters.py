"""
https://www.hackerrank.com/challenges/alternating-characters/problem
"""


def alternatingCharacters(s):
    """Implemented this first try, passing all test cases, earning 20 points,
    January 17, 2022."""
    current_character = s[0]
    delete_counter = 0
    
    for character in s[1:]:
        if character == current_character:
            delete_counter += 1
        else:
            current_character = character
    
    return delete_counter


assert alternatingCharacters('AABAAB') == 2
