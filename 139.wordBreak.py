class Solution:
    def wordBreak(self, s, wordDict):
        index = [True] + [False]*len(s)
        s = '0' + s
        for i in range(1, len(s)+1):
            for w in wordDict:
                l = len(w)
                if s[i+1-l:i+1] == w and index[i-l] is True:
                    index[i] = True
        print(s)
        print(index)
        return index[-1]       

s = "leetcode"
wordDict = ["leet", "code"]
sol = Solution()
res = sol.wordBreak(s, wordDict)
print(res)