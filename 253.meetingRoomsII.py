import heapq
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def minMeetingRooms(intervals):
    intervals.sort(key=lambda x: x.start)
    heap = []
    for item in intervals:
        if heap and item.start >= heap[0]:
            heapq.heapreplace(heap, item.end)
        else:
            heapq.heappush(heap, item.end)
    return len(heap)

intervals = [[13,15],[1,13]]
intervals = [Interval(item[0], item[1]) for item in intervals]
res = minMeetingRooms(intervals)
print(res)