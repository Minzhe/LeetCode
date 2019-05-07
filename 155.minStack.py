class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        
    def push(self, x: int) -> None:
        minval = self.getMin()
        if minval is not None:
            self.stack.append((x, min(minval, x)))
        else:
            self.stack.append((x, x))
        
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        
    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        
    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()