"""
https://www.hackerrank.com/challenges/repeated-string/problem
"""


def repeatedString(s, n):
    """Either 1,000,000,000,000

    The length of S could be less than N.
    The length of S could be greater than N
    The length of S could be equal to N
    """
    # The number of times the letter 'a' occurs in the string S.
    num_a = s.count('a')

    # If the length of S is less than N, there must be some number of times
    # that S wholy divides into N, and there may or may not be a remainder when
    # doing so.
    if len(s) < n:
        whole = n // len(s)
        remainder = n % len(s)
        # If the remainder is 0, then we just need to count the number of times
        # 'a' occurrs in S, and then multiply this by how many times S wholy
        # divides into N.
        if remainder == 0:
            answer = num_a * whole
            return answer
        else:
            return num_a * whole + s[:remainder].count('a')
    elif len(s) > n:
        return s[:n].count('a')

    return


def old_solution(s, n):
    """Didn't work on large inputs."""
    # The old, string-building method.  Didn't work on big inputs.
    new_s = ''
    number_of_times = 0
    print("starting")
    while len(new_s) < n:
        new_s += s
        number_of_times += 1
    print("stopped")

    print("Number of As", num_a)
    print("String:", new_s, len(new_s))
    a = new_s[:n]
    b = new_s[n:]
    print(a, b, b.count('a'))
    new_s = new_s[:n]
    print("String:", new_s, len(new_s))
    print("Number of times", number_of_times)
    
    total_number_of_a = num_a * number_of_times - b.count('a')
    print("Total number of a:", total_number_of_a)
            
    return total_number_of_a


if __name__ == '__main__':
    assert repeatedString("abcac", 10) == 4
    assert repeatedString("aba", 10) == 7
    assert repeatedString("a", 1000000000000) == 1000000000000
    assert repeatedString("udjlitpopjhipmwgvggazhuzvcmzhulowmveqyktlakdufzcefrxufssqdslyfuiahtzjjdeaxqeiarcjpponoclynbtraaawrps", 872514961806) == 69801196944
