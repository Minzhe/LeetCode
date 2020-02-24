class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        minval = self.getMin() if self.getMin() is not None else x
        if minval > x:
            self.stack.append((x, x))
        else:
            self.stack.append((x, minval))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]
        
    def getMin(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1][1]