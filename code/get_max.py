"""
Data structures > Stacks
https://www.hackerrank.com/challenges/maximum-element/problem

https://github.com/jguerra7/HackerRank-1/blob/master/data-structures/maximum-element.py
"""


def getMax(operations):
    """
    https://github.com/imsoumen/HackerRank/blob/master/Challenges/Maximum_Element.py

    This works using a second stack to somehow keep track of the maximum items
    observed in the operations (and which are present in the primary stack).
    """
    main_stack = []
    max_stack = [0]
    output = []

    for op in operations:
        query = op.split(" ")

        if query[0] == '1':
            num = int(query[1])
            main_stack.append(num)
            if max_stack[-1] <= num:
                max_stack.append(num)

        elif query[0] == '2':
            if main_stack[-1] == max_stack[-1]:
                max_stack.pop()
            main_stack.pop()

        elif query[0] == '3':
            output.append(max_stack[-1])

    return output


def getMax2(operations):
    """This method tries to use only one stack, but uses external-to-the-stack
    variables to keep track of the maximum element present in the stack."""
    q = []
    output = list()

    for op in operations:
        if len(op.split(" ")) == 2:
            _, x = op.split(" ")
            q.append(int(x))

        elif op == "2":
            q = q[:-1]

        elif op == "3":
            def find_max(q):
                max_so_far = -1
                for item in q:
                    if item > max_so_far:
                        max_so_far = item
                return max_so_far
            output.append(find_max(q))

    return output


if __name__ == '__main__':
    assert getMax(["1 97", "2", "1 20", "2", "1 26", "1 20", "2", "3", "1 91", "3"]) == [26, 91]
    assert getMax(["1 83", "3", "2", "1 76"]) == [83]
