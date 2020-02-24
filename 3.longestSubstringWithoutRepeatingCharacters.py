class Solution:
    def lengthOfLongestSubstring(self, s):
        maxlen, start = 0, 0
        lastseenin = dict()
        for i in range(len(s)):
            if s[i] in lastseenin and lastseenin[s[i]] >= start:
                start = lastseenin[s[i]] + 1
            else:
                maxlen = max(maxlen, i-start+1)
            lastseenin[s[i]] = i
        return maxlen

s = 'abcabcbb'
sol = Solution()
ans = sol.lengthOfLongestSubstring(s)
print(ans)