class Solution:
    def findCircleNum(self, M):
        n = len(M)
        parents = list(range(n))
        
        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            parents[rootx] = rooty
        
        for i in range(0, n-1):
            for j in range(i+1, n):
                if M[i][j] == 1:
                    union(i,j)
        
        circles = set(find(i) for i in range(n))
        return len(circles)
                