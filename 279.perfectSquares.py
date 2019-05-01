import math

class Solution:
    # def __init__(self):
    #     self.ans = [0]

    # def numSquares(self, n):
    #     while len(self.ans) < n + 1:
    #         i, j = len(self.ans), 1
    #         self.ans.append(i)
    #         while j * j <= i:
    #             self.ans[i] = min(self.ans[i], self.ans[i-j*j]+1)
    #             j += 1
    #         i += 1
    #     return self.ans[n]

    def numSquares(self, n):
        Q = [[n]]
        while Q:
            sol = Q.pop(0)
            x = int(math.sqrt(sol[-1]))
            for i in range(x, 0, -1):
                if i * i == sol[-1]:
                    return len(sol)
                else:
                    Q.append(sol[:-1] + [i*i, sol[-1]-i*i])

sol = Solution()
res = sol.numSquares(12)
print(res)
        