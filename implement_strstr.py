"""
This solution really taught me to break out that inner while loop into its own
function call, because I was getting bugs involving Python's behavior of nested
while loops, and trying to break out with "break" and "continue"  I got it
working, but things were more CLEAR when you break it out into a function.

Just submitted this but it wouldn't work on a crazy big input.  Looking back,
you really are just moving down the line naively.

Now I'm thinking to use binary_search or anything algorithm to first find the
first character.  That's a good bet.  January 18, 2022
"""


def condition(j, haystack, needle):
    travel_distance = 0
    while travel_distance < len(needle):
        if haystack[j+travel_distance] == needle[travel_distance]:
            travel_distance += 1
        else:
            return False
    return True


def strstr(haystack, needle):
    if len(needle) == 0:
        return 0
    i = 0

    while (i+len(needle)) <= len(haystack):
        # Let's begin a travel at position i, and walk only the distance the
        # length of the needle, at most.
        j = i
        if condition(j, haystack, needle):
            return i
        else:
            i += 1

    return -1


assert strstr("hello", "ll") == 2
assert strstr("", "") == 0
assert strstr("a", "a") == 0
