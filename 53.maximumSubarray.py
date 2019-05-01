class Solution:
    def maxSubArray(self, nums):
        s = [None for i in range(len(nums))]
        s[0] = nums[0]
        for i in range(1, len(s)):
            if s[i-1] <= 0:
                s[i] = nums[i]
            else:
                s[i] = s[i-1] + nums[i]
        return max(s)