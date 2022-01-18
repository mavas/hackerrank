def _method_1(a, b):
    """Thought of this, on the fly, January 15, 2022."""
    import string
    o = 0

    for character in string.ascii_lowercase:
        a_count = a.count(character)
        b_count = b.count(character)
        difference = abs(a_count - b_count)
        if difference > 0:
            o += difference

    return o

def _method_2(a, b):
    """First thought of this method, involving using dictionaries keyed by
    letter of the alphabet, and valued by number of occurrences.  This is
    incomplete and does not work yet."""
    c1 = dict()
    c2 = dict()
    
    for c in a:
        if c in c1:
            c1[c] += 1
        else:
            c1[c] = 1
    
    for c in b:
        if c in c2:
            c2[c] += 1
        else:
            c2[c] = 1

def makeAnagram(a, b):
    """Computes the number of deletions necessary to make both strings
    anagrams."""
    o = 0  # The number of deletions
    return _method_1(a, b)
    return o
 

if __name__ == '__main__':
    assert makeAnagram('cde', 'abc') == 4
