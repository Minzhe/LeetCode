class Solution:
    def validTree(self, n, edges):
        if len(edges) != n-1: return False
        parents = list(range(n))
        
        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            if rootx == rooty:
                return False
            parents[rootx] = rooty
            return True
        
        for x, y in edges:
            if not union(x, y):
                return False
        return True