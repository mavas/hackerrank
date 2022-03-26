"""
https://www.hackerrank.com/challenges/ctci-ransom-note/problem

Trying again March 26, 2022
"""


def _solve_method_2(magazine, note):
    note = note.split()
    note_d = dict()
    for w in note:
        if not w in note_d:
            note_d[w] = 1
        else:
            note_d[w] += 1

    magazine = magazine.split()
    for w in magazine:
        if w in note_d:
            if note_d[w] == 1:
                del note_d[w]
            else:
                note_d[w] -= 1

    return len(note_d) == 0


def _solve_method_1(magazine, note):
    """This method works on small inputs but produced a timeout.  It doesn't
    use dictionaries ironically."""
    magazine = magazine.split()
    note = note.split()

    for w in note:
        if not w in magazine:
            return False
        else:
            magazine.remove(w)

    return True


def ransom_note(magazine, note):
    return _solve_method_2(magazine, note)


if __name__ == '__main__':
    assert ransom_note('attack at dawn', 'Attack at dawn') == False
    assert ransom_note('give me one grand today night', 'give one grand today') == True
    assert ransom_note('two times three is not four', 'two times two is four') == False
