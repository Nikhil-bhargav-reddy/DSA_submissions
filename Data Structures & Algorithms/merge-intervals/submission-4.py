class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda i:i[0]) # sort by start
        res = []

        for i in intervals:
            if res and res[-1][1] >= i[0]: # if end of prev is > start of new, then merging
                res[-1][1] = i[1]
            else:
                res.append(i)
        return res