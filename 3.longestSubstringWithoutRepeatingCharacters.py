class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, max_len = 0, 0
        char_idx = {}
        for i in range(len(s)):
            if s[i] in char_idx.keys() and start <= char_idx[s[i]]:
                start = char_idx[s[i]] + 1
            else:
                max_len  = max(max_len, i-start+1)
            char_idx[s[i]] = i          
        return max_len