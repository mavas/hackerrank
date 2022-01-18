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
