from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        maxlen, start = 0, 0
        lastseen = dict()

        for i, char in enumerate(s):
            lastseen[char] = i
            if len(lastseen) > 2:
                earlyseen = min(lastseen.values())
                del lastseen[s[earlyseen]]
                start = earlyseen + 1
            maxlen = max(maxlen, i-start+1)
        
        return maxlen

    # def lengthOfLongestSubstringTwoDistinct(self, s):
    #     maxlen, start = 0, 0
    #     self.last2seen = defaultdict(lambda: (None, None))

    #     for i in range(len(s)):
    #         idx = self.last2seen[s[i]][1]
    #         if idx is not None and idx >= start:
    #             start = idx + 1
    #         else:
    #             maxlen = max(maxlen, i-start+1)
    #         self.update(s[i], i)
    #         print(i, start, maxlen, idx, self.last2seen)
    #     return maxlen
    
    # def update(self, x, i):
    #     self.last2seen[x] = (i, self.last2seen[x][0])

# s = 'eceba'
# sol = Solution()
# ans = sol.lengthOfLongestSubstringTwoDistinct(s)
# print(ans)