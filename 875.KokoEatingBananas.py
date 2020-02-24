class Solution:
    def minEatingSpeed(self, piles, H):
        lower, upper = max(sum(piles) // H, 1), max(piles)

        while lower < upper:
            size = (lower + upper) // 2
            hours = self.hoursNeeded(piles, size)
            if hours <= H:
                upper = size
            else:
                lower = size + 1
        
        return lower
    
    def hoursNeeded(self, piles, size):
        hours = 0
        for pile in piles:
            hours += -(-pile // size)
        return hours