from collections import defaultdict

class Solution:
    def minDominoRotations(self, A, B):
        countA, countB, countSame = defaultdict(int), defaultdict(int), defaultdict(int)
        for i in range(len(A)):
            countA[A[i]] += 1
            countB[B[i]] += 1
            if A[i] == B[i]:
                countSame[A[i]] += 1
        for i in range(1, 7):
            if (countA[i] + countB[i] - countSame[i]) == len(A):
                return min(countA[i] - countSame[i], countB[i] - countSame[i])
        return -1


A = [2,1,2,4,2,2]
B = [5,2,6,2,3,2]
sol = Solution()
ans = sol.minDominoRotations(A, B)
print(ans)