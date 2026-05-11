class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        # sort the intervals by start time
        # overalp? if prev end < current start, overlap exists, we can keep start as is, we do max(end,nextend)
        intervals.sort(key=lambda i:i[0])
        print(intervals)

        for i in intervals:
            if res and res[-1][1] >= i[0]:
                res[-1][1] =  max(res[-1][1], i[1]) 
            else:
                res.append(i)
        return res