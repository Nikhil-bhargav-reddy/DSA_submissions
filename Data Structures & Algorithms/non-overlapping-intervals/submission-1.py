class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        res = []

        intervals.sort(key= lambda i:i[1])

        counter = 0

        for i in intervals:
            if res and res[1] > i[0]: # overlap so remove I
                counter+=1
            else:
                res = i

        return counter