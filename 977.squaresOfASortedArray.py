import collections

class Solution:
    def sortedSquares(self, A):
        ans = collections.deque([])
        l, r = 0, len(A) - 1
        while l <= r:
            print(l,r)
            ln, rn = A[l], A[r]
            if abs(ln) < abs(rn):
                ans.appendleft(rn*rn)
                r -= 1
            else:
                ans.appendleft(ln*ln)
                l += 1
        return list(ans)