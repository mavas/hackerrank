"""
https://leetcode.com/problems/valid-parentheses/

Completed and passed January 18, 2022
"""


def is_valid(s):
    stack = []

    for item in s:
        if len(stack) > 0:
            top_of_stack = stack[-1]
            if top_of_stack == '(' and item == ')':
                stack = stack[:-1]
                continue
            elif top_of_stack == '[' and item == ']':
                stack = stack[:-1]
                continue
            elif top_of_stack == '{' and item == '}':
                stack = stack[:-1]
                continue
        stack.append(item)

    return len(stack) == 0


assert is_valid('()') == True
assert is_valid('()[]{}') == True
assert is_valid('(]') == False
