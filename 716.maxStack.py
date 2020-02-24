class MaxStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [(None, None, None)]

    def push(self, x):
        maxval, maxidx = self.peekMax(), self.peekMaxIndex()
        if maxval is None or maxidx > x:
            self.stack.append((x, maxval, maxidx))
        else:
            idx = len(self.stack) + 1
            if idx > maxidx:
                self.stack.append((x, x, idx))
            else:
                self.stack.append((x, x, maxidx))

    def pop(self):
        self.stack = self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def peekMax(self):
        return self.stack[-1][1]
    
    def peekMaxIndex(self):
        return self.stack[-1][2]

    def popMax(self):
        maxval, maxidx = self.peekMax(), self.peekMaxIndex()
        if maxidx is not None:
            self.stack = self.stack[:maxidx] + self.stack[(maxidx+1):]
        return maxval
