"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
# 0,1,2,3,4,5,6,7,8,9,......30
# 5,6,7,8,9,10
# 15,16,.....20intervals.sort(key = lambda i:i[0])
        intervals.sort(key = lambda i:i.start)


        for i in range(len(intervals)):
            if i >0 and intervals[i].start < intervals[i-1].end:
                return False
        return True
