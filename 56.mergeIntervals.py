# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        merged = []
        for interval in sorted(intervals, key=lambda x: x.start):
            if merged and interval.start <= merged[-1].end:
                merged[-1].end = max(interval.end, merged[-1].end)
            else:
                merged.append(interval)
        return merged
        