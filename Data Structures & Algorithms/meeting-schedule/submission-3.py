"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key = lambda x:x.start)

        # print(intervals)

        prev = None

        for i in intervals:
            if prev and prev.end> i.start:
                return False
            else:
                prev = i
        return True