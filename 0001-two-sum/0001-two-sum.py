class Solution(object):
    def twoSum(self, nums, target):
        nums_dict=dict()
        for idx, val in enumerate(nums):
            if (target-val) in nums_dict:
                return [nums_dict[target-val], idx]
            nums_dict[val]=idx
        return None