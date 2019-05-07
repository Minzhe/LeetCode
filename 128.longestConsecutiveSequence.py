class Solution:
    def longestConsecutive(self, nums):
        nums = set(nums)
        ans = 0
        while nums:
            begin = end = nums.pop()
            while begin - 1 in nums:
                begin -= 1
                nums.remove(begin)
            while end + 1 in nums:
                end += 1
                nums.remove(end)
            ans = max(ans, end - begin + 1)
        return ans

nums = [100,4,200,1,3,2]      
sol = Solution()
ans = sol.longestConsecutive(nums)
print(ans)