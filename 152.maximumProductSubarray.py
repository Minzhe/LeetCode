class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxp = [None for i in range(len(nums))]
        minp = [None for i in range(len(nums))]
        maxp[0] = minp[0] = nums[0]
        for i, x in enumerate(nums[1:], 1):
            cand = [maxp[i-1]*x, minp[i-1]*x, x]
            maxp[i] = max(cand)
            minp[i] = min(cand)
        return max(maxp)
