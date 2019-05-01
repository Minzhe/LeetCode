class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        seen = [[beginWord]]
        unseen = set(wordList)
        ans, seen_epoc, changes = [], [], 0
        while seen:
            print('+', seen)
            words, new_see = seen.pop(0), []
            last = words[-1]
            # if len(wor)
            if ans and len(words) > len(ans[0]):
                return ans
            # change one character
            for i in range(len(last)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    new = last[:i] + char + last[i+1:]
                    if new in unseen:
                        new_seq = words + [new]
                        if new == endWord:
                            ans.append(new_seq)
                        else:
                            seen_epoc.append(new)
                            if len(new_seq) > len(words):
                                changes += 1
                                unseen = unseen - set(seen_epoc)
                                seen_epoc = []
                            seen.append(words + [new])
                            print('-', seen)
                            print('*', unseen)
        return ans

# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# wordList = ["hot","dot","dog","lot","log"]
beginWord = "red"
endWord = "tax"
wordList = ["ted","tex","red","tax","tad","den","rex","pee"]
sol = Solution()
res = sol.findLadders(beginWord, endWord, wordList)
print(res)