import collections
class Solution:
    def wordBreak(self, s, wordDict):
        index = collections.defaultdict(list)
        for i in range(len(s)):
            # print(index)
            for j in range(len(wordDict)):
                w = wordDict[j]
                l = len(w)
                if s[i+1-l:i+1] == w:
                    if i+1-l == 0:
                        index[i].append(w)
                    elif len(index[i-l]) > 0:
                        for item in index[i-l]:
                            index[i].append(item + ' ' + w)
        return index[max(index.keys())]

# s = "leetcode"
# wordDict = ["leet", "code"]
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
s = "pineapplepenapple"
wordDict = ["apple","pen","applepen","pine","pineapple"]
# s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
sol = Solution()
res = sol.wordBreak(s, wordDict)
print(res)