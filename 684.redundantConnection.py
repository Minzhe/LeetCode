from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges):
        parent = defaultdict(int)

        def find(x):
            return x if parent[x] == 0 else find(parent[x])
        
        def union(x, y):
            rootx, rooty = find(x), find(y)
            parent[rootx] = rooty
            return rootx != rooty
        
        for (x, y) in edges:
            if not union(x, y):
                return [x, y]

edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
sol = Solution()
sol.findRedundantConnection(edges)
