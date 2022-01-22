"""
https://leetcode.com/problems/valid-palindrome
"""


def using_isalnum(s):
    s = ''.join(filter(str.isalnum, s))
    return s


def using_string_module(s):
    o = ''
    import string
    for character in s:
        if character in string.ascii_lowercase:
            o += character
    return o


def valid_palindrome(s):
    s = s.lower()
    s = using_isalnum(s)

    middle_index = len(s) // 2
    first_half = s[:middle_index]
    if (len(s) % 2) == 0:
        second_half = s[middle_index:]
    else:
        second_half = s[middle_index+1:]
    second_half = second_half[::-1]

    i = 0
    while i < len(first_half):
        if first_half[i] == second_half[i]:
            i += 1
            continue
        else:
            return False
    return True


if __name__ == '__main__':
    assert valid_palindrome("A man, a plan, a canal: Panama") == True
    assert valid_palindrome("race a car") == False
    assert valid_palindrome(" ") == True
    assert valid_palindrome("ab") == False
