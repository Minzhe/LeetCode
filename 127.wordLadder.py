class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList: return 0
        seen = [[endWord]]
        unseen = set(wordList)
        while seen:
            words, new_see = seen.pop(0), []
            last = words[-1]
            # change one character
            for i in range(len(last)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    new = last[:i] + char + last[i+1:]
                    if new == beginWord: 
                        print(new, beginWord)
                        return len(words) + 1
                    if new in unseen:
                        seen.append(words + [new])
                        unseen.remove(new)
        return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
wordList = ["hot","dot","dog","lot","log"]
sol = Solution()
res = sol.ladderLength(beginWord, endWord, wordList)
print(res)