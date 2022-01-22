"""
https://leetcode.com/problems/two-sum/


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        decorated_nums = []
        for index, item in enumerate(nums):
            decorated_nums.append((item, index))
        
        for i in decorated_nums:
            for j in decorated_nums:
                if (i[0] + j[0]) == target:
                    if i[1] != j[1]:
                        return [i[1], j[1]]

Today this algorithm succeeded, however.  It remained the same since the first
time I tried/submitted more than a week ago, so oh well.
"""

#def twoSum2(nums: List[int], target: int) -> List[int]:
def twoSum2(nums, target):
    decorated_nums = []
    for index, item in enumerate(nums):
        decorated_nums.append((item, index))
    import itertools
    for i, j in itertools.combinations(nums, 2):
        if (i + j) == target:
            return [i, j]
        
def twoSum(nums, target):
    decorated_nums = []
    for index, item in enumerate(nums):
        decorated_nums.append((item, index))
    
    import itertools
    for i, j in itertools.combinations(decorated_nums, 2):
    #for i in decorated_nums:
        if (i[0] + j[0]) == target:
            if i[1] != j[1]:
                return [i[1], j[1]]


if __name__ == '__main__':
    assert twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert twoSum([3, 2, 4], 6) == [1, 2]
    assert twoSum([3, 3], 6) == [0, 1]
