# January 18, 2022
#Passed today.  I had to modify the code to account for the [9] case, which was
#fun.


def plus_one(digits):
    N = len(digits)
    i = N - 1

    while i >= 0:
        if digits[i] == 9:
            digits[i] = 0
            i -= 1
            if i == -1:
                digits = [1] + digits
                return digits
        else:
            digits[i] = digits[i] + 1
            return digits


assert plus_one([1, 2, 3]) == [1, 2, 4]
assert plus_one([4, 3, 2, 1]) == [4, 3, 2, 2]
assert plus_one([9]) == [1, 0]
