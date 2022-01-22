"""
https://leetcode.com/problems/palindrome-number

Completed this January 19, 2022 in a single shot, passing all test cases.

In LeetCode's editor, it suggested a followup question regarding this
particular problem: "could you solve the problem without converting the integer
to a string?"  Indeed, my first thought solution did involve converting to
string, but it did pass efficiently and correctly the very first time, so I
guess my default intuition about this solution and problem were not off or
astray from what most people would think and do.

    // Special cases:
    // As discussed above, when x < 0, x is not a palindrome.
    // Also if the last digit of the number is 0, in order to be a palindrome,
    // the first digit of the number also needs to be 0.
    // Only 0 satisfy this property.
    if(x < 0 || (x % 10 == 0 && x != 0)) {
        return false;
    }

    int revertedNumber = 0;
    while(x > revertedNumber) {
        revertedNumber = revertedNumber * 10 + x % 10;
        x /= 10;
    }

    // When the length is an odd number, we can get rid of the middle digit by revertedNumber/10
    // For example when the input is 12321, at the end of the while loop we get x = 12, revertedNumber = 123,
    // since the middle digit doesn't matter in palidrome(it will always equal to itself), we can simply get rid of it.
    return x == revertedNumber || x == revertedNumber/10;
"""
def isPalindrome(x):
    x = str(x)
    middle_index = len(x) // 2

    first_half = x[:middle_index]
    if (len(x) % 2) == 0:
        second_half = x[middle_index:]
    else:
        second_half = x[middle_index+1:]
    second_half = second_half[::-1]

    for index, character in enumerate(first_half):
        if second_half[index] == character:
            continue
        else:
            return False
    
    return True


if __name__ == '__main__':
    assert isPalindrome(121) == True
