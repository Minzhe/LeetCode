import collections
class Solution:
    def coinChange(self, coins, amount):
        inf = float('inf')
        ans = collections.defaultdict(lambda: inf)
        ans[0] = 0
        for i in range(1, amount+1):
            num = [ans[i-c]+1 for c in coins]
            ans[i] = min(num)
        return ans[amount] if ans[amount] != inf else -1

coins = [1,2,5]
amount = 11
sol = Solution()
res = sol.coinChange(coins, amount)
print(res)