"""
https://leetcode.com/problems/roman-to-integer/
"""


def roman_to_integer(s):
    """
    This implementation passed all tests on submission January 18, 2022.

    There's not too much any other way of implementing this, am I right?  You
    really just have encode each of the rules that are stated.
    """
    o = list()
    did_a_skip = False

    for index, item in enumerate(s):
        if did_a_skip:
            did_a_skip = not did_a_skip
            continue

        if item == 'V':
            o.append(5)
        elif item == 'L':
            o.append(50)
        elif item == 'D':
            o.append(500)

        if item == 'I':
            if (index+1) != len(s):
                next_value = s[index+1]
                if next_value == 'V':
                    o.append(4)
                    did_a_skip = True
                elif next_value == 'X':
                    o.append(9)
                    did_a_skip = True
                else:
                    o.append(1)
            else:
                o.append(1)
        elif item == 'X':
            if (index+1) != len(s):
                next_value = s[index+1]
                if next_value == 'L':
                    o.append(40)
                    did_a_skip = True
                elif next_value == 'C':
                    o.append(90)
                    did_a_skip = True
                else:
                    o.append(10)
            else:
                o.append(10)
        elif item == 'C':
            if (index+1) != len(s):
                next_value = s[index+1]
                if next_value == 'D':
                    o.append(400)
                    did_a_skip = True
                elif next_value == 'M':
                    o.append(900)
                    did_a_skip = True
                else:
                    o.append(100)
            else:
                o.append(100)

        elif item == 'M':
            o.append(1000)

    return sum(o)


if __name__ == '__main__':
    assert roman_to_integer("III") == 3
    assert roman_to_integer("MCMXCIV") == 1994
    assert roman_to_integer("DCXXI") == 621
