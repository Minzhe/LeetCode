class MyQueue:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.quene = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        """
        self.quene.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        """
        x = self.quene[0]
        self.quene = self.quene[1:]
        return x
        

    def peek(self):
        """
        Get the front element.
        """
        return self.quene[0]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        """
        return True if len(self.quene) == 0 else False