class Solution:
    def canAttendMeetings(self, intervals):
        end = 0
        for interval in sorted(intervals, key=lambda x: x[0]):
            if interval[0] < end:
                return False
            else:
                end = interval[1]
        return True