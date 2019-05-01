class Solution:
    def shortestDistance(self, words, word1, word2):
        length = len(words)
        idx1, idx2, ans = length, length, length
        for i in range(length):
            if words[i] == word1:
                idx1 = i
                ans = min(ans, abs(idx2-i))
            elif words[i] == word2:
                idx2 = i
                ans = min(ans, abs(idx1-i))
        return ans