import collections

class MovingAverage:
    def __init__(self, size):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.deque = collections.deque([])


    def next(self, val):
        self.deque.append(val)
        if len(self.deque) > self.size:
            self.deque.popleft()
        return sum(self.deque) / len(self.deque)
