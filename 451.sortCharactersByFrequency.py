import collections
class Solution:
    def frequencySort(self, s):
        freq = collections.defaultdict(int)
        for i in s:
            freq[i] += 1
        keys = sorted(freq.keys(), key=lambda x: -freq[x])
        
        sort_s = ''
        for x in keys:
            sort_s += x*freq[x]

        return sort_s

s = "tree"
sol = Solution()
sol.frequencySort(s)