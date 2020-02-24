class Solution:
    def validTree(self, n, edges):
        parent = list(range(n))

        def find(x):
            return x if parent[x] == x else find(parent[x])
        
        def union(x, y):
            rootx, rooty = find(x), find(y)
            parent[rootx] = rooty
            return rootx != rooty
        
        for (x, y) in edges:
            if not union(x, y):
                return False
        
        return len(edges) == (n - 1)