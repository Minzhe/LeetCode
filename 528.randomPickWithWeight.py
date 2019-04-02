import itertools
import random
import bisect

class Solution:
    def __init__(self, w):
        self.cdf = list(itertools.accumulate(w))

    def pickIndex(self):
        x = random.randint(1, self.cdf[-1])
        return bisect.bisect_left(self.cdf, x)