class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        if len(words1) != len(words2):
            return False

        parent = dict()

        def find(x):
            if x not in parent:
                parent[x] = x
            return x if parent[x] == x else find(parent[x])
        
        def union(x, y):
            rootx, rooty = find(x), find(y)
            parent[rootx] = rooty

        for w1, w2 in pairs:
            union(w1, w2)
        
        for w1, w2 in zip(words1, words2):
            if w1 != w2 and find(w1) != find(w2):
                return False
        
        return True
        