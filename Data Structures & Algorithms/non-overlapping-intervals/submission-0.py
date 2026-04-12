class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals_removed = 0

        intervals.sort(key =lambda i: i[1])

        # sort by end of interval to move big intervals to the end to remove
        res = []
        for i in intervals:
            if res and res[-1][1] > i[0]:
                intervals_removed+=1

            else:
                res.append(i)
        
        return intervals_removed