def cookies(k, A):
    def satisfy(k, A):
        for item in A:
            if item < k:
                return False
        return True

    def select_least_two_indeces(A):
        first = 0
        second = 1
        for item, index in enumerate(A[2:]):
            if item != first:
                second = item
        return first, second

    r = -1
    while not satisfy(k, A):
        a = sorted(set(A))[0]
        b = sorted(set(A))[0]
        print(a, b)
        break

    return r


if __name__ == '__main__':
    assert cookies(9, [2, 7, 3, 6, 4, 6]) == 4
