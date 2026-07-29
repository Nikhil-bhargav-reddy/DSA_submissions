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

        print(intervals)

        prev = []

        for i in intervals:
            if prev and prev[-1].end> i.start:
                return False
            elif prev:
                prev[0] = i
            else: 
                prev.append(i)
        return True