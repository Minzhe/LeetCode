import collections
class Logger:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.messageTime = collections.defaultdict(lambda: -1)

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        prev, diff = self.messageTime[message], timestamp - self.messageTime[message]
        if prev == -1:
            self.messageTime[message] = timestamp
            return True
        else:
            if diff >= 10:
                self.messageTime[message] = timestamp
                return True
            else:
                return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)