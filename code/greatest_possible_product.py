"""
https://apply.workable.com/screenly/j/CD139FE47C/apply/

Finally it would greatly help our final evaluation process if you could provide
me with a slightly more complex example of your programming.

Consider the following problem: Given an array of positive integers, return the
greatest possible product among any two integers in the array. I.e. find a[i] *
a[j] such that i != j and a[i] * a[j] is the greatest possible. What would your
solution be in your preferred programming language? The solution is only a few
lines of code, so it shouldn't take too long. Please send me your completed
source code with a description of why you choose your particular
implementation.
"""


def greatest_possible_product(a):
    a.sort()
    return a[-1] * a[-2]
 

if __name__ == '__main__':
    assert greatest_possible_product([2, 540, 21, 24, 9]) == 12960
