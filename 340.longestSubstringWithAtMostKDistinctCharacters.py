class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        maxlen, start = 0, 0
        lastseen = dict()

        for i, char in enumerate(s):
            lastseen[char] = i
            if len(lastseen) > k:
                earlyseen = min(lastseen.values())
                del lastseen[s[earlyseen]]
                start = earlyseen + 1
            maxlen = max(maxlen, i-start+1)
        
        return maxlen