class Solution:
    def isInterleave(self, s1, s2, s3):
        # DP
        m, n, s = len(s1), len(s2), len(s3)
        if m + n != s: return False
        arr = [[True] * (n+1) for i in range(m+1)]
        # s1 start match
        for i in range(m):
            arr[i+1][0] = arr[i][0] and s1[i] == s3[i]
        # s2 start match
        for j in range(n):
            arr[0][j+1] = arr[0][j] and s2[j] == s3[j]
        # update rest with dp
        for i in range(1, m+1):
            for j in range(1, n+1):
                match1 = arr[i][j-1] and (s2[j-1] == s3[i+j-1])
                match2 = arr[i-1][j] and (s1[i-1] == s3[i+j-1])
                arr[i][j] = match1 or match2
        print(arr)
        return arr[m][n]

        # # Recursion
        # if len(s1) + len(s2) != len(s3): return False
        # if len(s1) == 0: return True if s2 == s3 else False
        # if len(s2) == 0: return True if s1 == s3 else False
        # if s1[0] == s2[0] == s3[0]:
        #     return self.isInterleave(s1[1:], s2, s3[1:]) or self.isInterleave(s1, s2[1:], s3[1:])
        # elif s1[0] == s3[0]:
        #     return self.isInterleave(s1[1:], s2, s3[1:])
        # elif s2[0] == s3[0]:
        #     return self.isInterleave(s1, s2[1:], s3[1:])
        # else:
        #     return False
                
# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbcbcac"
s1="db"
s2="b"
s3="cbb"
sol = Solution()
res = sol.isInterleave(s1, s2, s3)
print(res)