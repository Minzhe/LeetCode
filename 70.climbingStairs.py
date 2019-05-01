class Solution:
    def climbStairs(self, n):
        if n == 1: return 1
        ans = [0 for i in range(n)]
        ans[0] = 1
        ans[1] = 2
        for i in range(2, n):
            ans[i] = ans[i-2] + ans[i-1]
        return ans[n-1]