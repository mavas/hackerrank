"""
https://www.hackerrank.com/challenges/one-week-preparation-kit-countingsort1/problem

I read the problem description, and never heard of this sort before, but am
excited to implement it since it sounds pretty easy and interesting. For some
reason they want you to return the frequency array, and not the sorted array,
and wants you to do it for all values between 0 and 100.
"""


def counting_sort_2(arr):
    """This is optional, and returns the sorted array, and doesn't go all the
    way to 100."""
    minimum_value = 100
    maximum_value = 0
    for item in arr:
        if item < minimum_value:
            minimum_value = item
        elif item > maximum_value:
            maximum_value = item

    N = abs(maximum_value - minimum_value) + 1
    frequency_arr = [0] * N
    for value in arr:
        frequency_arr[value] += 1

    output = []
    for index, item in enumerate(frequency_arr):
        output += [index] * item

    return output


def counting_sort(arr):
    frequency_arr = [0] * 100
    for value in arr:
        frequency_arr[value] += 1
    return frequency_arr


if __name__ == '__main__':
    a = [63, 25, 73, 1, 98, 73, 56, 84, 86, 57, 16, 83, 8, 25, 81, 56, 9, 53, 98, 67, 99, 12, 83, 89, 80, 91, 39, 86, 76, 85, 74, 39, 25, 90, 59, 10, 94, 32, 44, 3, 89, 30, 27, 79, 46, 96, 27, 32, 18, 21, 92, 69, 81, 40, 40, 34, 68, 78, 24, 87, 42, 69, 23, 41, 78, 22, 6, 90, 99, 89, 50, 30, 20, 1, 43, 3, 70, 95, 33, 46, 44, 9, 69, 48, 33, 60, 65, 16, 82, 67, 61, 32, 21, 79, 75, 75, 13, 87, 70, 33]
    b = [0, 2, 0, 2, 0, 0, 1, 0, 1, 2, 1, 0, 1, 1, 0, 0, 2, 0, 1, 0, 1, 2, 1, 1, 1, 3, 0, 2, 0, 0, 2, 0, 3, 3, 1, 0, 0, 0, 0, 2, 2, 1, 1, 1, 2, 0, 2, 0, 1, 0, 1, 0, 0, 1, 0, 0, 2, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 2, 1, 3, 2, 0, 0, 2, 1, 2, 1, 0, 2, 2, 1, 2, 1, 2, 1, 1, 2, 2, 0, 3, 2, 1, 1, 0, 1, 1, 1, 0, 2, 2]
    assert counting_sort(a) == b
    assert counting_sort_2([1, 0, 1, 3, 2, 1]) == [0, 1, 1, 1, 2, 3]
