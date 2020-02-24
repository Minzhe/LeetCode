class TrieNodes(object):
    def __init__(self):
        self.sent = None
        self.hot = 0
        self.child = dict()
        self.end = False

class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.root = TrieNodes()
        self.kw = ''
        for sent, time in zip(sentences, times):
            self.add_record(sent, time)
        
    def add_record(self, sent, time):
        p = self.root
        for w in sent:
            if w not in p.child:
                p.child[w] = TrieNodes()
            p = p.child[w]
        p.end = True
        p.sent = sent
        p.hot -= time
    
    def search(self, kw):
        p = self.root
        for w in kw:
            if w not in p.child:
                return []
            p = p.child[w]
        return self.dfs(p)
    
    def dfs(self, root):
        ans = []
        if root:
            if root.end:
                ans.append((root.hot, root.sent))
            for w in root.child:
                ans.extend(self.dfs(root.child[w]))
        return ans

    def input(self, c):
        ans = []
        if c == '#':
            self.add_record(self.kw, 1)
            self.kw = ''
        else:
            self.kw += 'c'
            ans = self.search(self.kw)
        return [sent for time, sent in sorted(ans)[:3]]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)