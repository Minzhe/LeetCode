from collections import defaultdict

class Solution:
    def longestStrChain(self, words):
        ans = defaultdict(int)
        for w in sorted(words, key=len):
            predecessors = [w[:i]+w[i+1:] for i in range(len(w))]
            ans[w] = max([ans[p] for p in predecessors]) + 1
        return max(ans.values())