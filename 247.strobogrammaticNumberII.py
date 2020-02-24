class Solution:
    def __init__(self):
        self.ans = dict()
        self.ans[1] = ['0', '1', '8']
        self.ans[2] = ['11', '88', '69', '96']

    def findStrobogrammatic(self, n):
        evenCand = ['00', '11', '88', '69', '96']
        oddCand = ['0', '1', '8']
        if n in self.ans:
            return self.ans[n]
        else:
            new_ans = []
            if n % 2 == 1:
                ans = self.findStrobogrammatic(n - 1)
                for cand in oddCand:
                    new_ans.extend(self.insert(ans, cand))
            else:
                ans = self.findStrobogrammatic(n - 2)
                for cand in evenCand:
                    new_ans.extend(self.insert(ans, cand))
            self.ans[n] = new_ans
        return self.ans[n]
    
    def insert(self, arr, x):
        n = int(len(arr[0]) / 2)
        return [s[:n] + x + s[(-n):] for s in arr]


n = 5
sol = Solution()
ans = sol.findStrobogrammatic(n)
print(ans)