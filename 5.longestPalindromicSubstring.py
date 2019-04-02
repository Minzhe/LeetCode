class Solution:
    def longestPalindrome(self, s: str) -> str:
        long_pal = ''
        for i in range(len(s)):
            # odd case: 'aba'
            pal = self.getPalindrome(s, i, i)
            long_pal = pal if len(pal) > len(long_pal) else long_pal
            # even case: 'abba'
            pal = self.getPalindrome(s, i, i+1)
            long_pal = pal if len(pal) > len(long_pal) else long_pal
        return long_pal

    def getPalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

