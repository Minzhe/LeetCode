from collections import defaultdict

class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        if len(words1) != len(words2):
            return False

        similar = defaultdict(set)
        for w1, w2 in pairs:
            similar[w1].add(w2)
            similar[w2].add(w1)
        
        for w1, w2 in zip(words1, words2):
            if w1 != w2 and w1 not in similar[w2]:
                return False
        
        return True
        