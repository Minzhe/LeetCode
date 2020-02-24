class Solution:
    def shipWithinDays(self, weights, D):
        lower, upper = max(weights), sum(weights)

        while lower < upper:
            size = (lower + upper) // 2
            days = self.daysNeeded(weights, size)
            if days <= D:
                upper = size
            else:
                lower = size + 1
        return lower
    
    def daysNeeded(self, weights, size):
        load, days = 0, 1
        for w in weights:
            if load + w  <= size:
                load += w
            else:
                load = w
                days += 1
        return days
