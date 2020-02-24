class Solution:
    def findCircleNum(self, M):
        parent = list(range(len(M)))

        def find(x):
            return x if parent[x] == x else find(parent[x])
        
        def union(x, y):
            rootx, rooty = find(x), find(y)
            parent[rootx] = rooty
            return rootx != rooty

        for i in range(1, len(M)):
            for j in range(0, i):
                if M[i][j] == 1:
                    union(i, j)
        
        return len(set(find(x) for x in parent))


M = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
sol = Solution()
ans = sol.findCircleNum(M)
print(ans)