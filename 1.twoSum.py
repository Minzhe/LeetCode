class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        if len(nums) < 2:
            return 'Array too short!'
        diff_idx = {}
        for i in range(len(nums)):
            if nums[i] in diff_idx.keys():
                return [diff_idx[nums[i]], i]
            else:
                diff_idx[target - nums[i]] = i
        return 'No answer'