class Solution:
    def expand(self, S):
        ans = ['']
        for item in S.replace('{', ' ').replace('}', ' ').split(' '):
            ans = [prefix + char for prefix in ans for char in item.split(',')]
        return sorted(ans)


s = '{a,b}c{d,e}f'
sol = Solution()
sol.expand(s)