def minimumAbsoluteDifference(arr):
    """This is what I whipped up first, and then I submitted it, and it looks
    like it failed on some test cases specifically due to run time; but surely,
    a lot of the test cases pass, so it's likely an efficiency problem, because
    surely this method isn't too efficient, but good first try to pass some
    cases.  January 17, 2022"""
    lowest_so_far = 100000
    
    for index_i, i in enumerate(arr):
        for index_j, j in enumerate(arr):
            if index_i != index_j:
                result = abs(i - j)
                if result < lowest_so_far:
                    lowest_so_far = result
 
    return lowest_so_far


if __name__ == '__main__':
	assert minimumAbsoluteDifference([3, -7, 0]) == 3
