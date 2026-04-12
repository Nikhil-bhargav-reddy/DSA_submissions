class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l=0
        newinterval_flag = False
        res= []

        if not intervals:
            res.append(newInterval)
            return res
        while l<len(intervals):
            if intervals[l][1] < newInterval[0]:
                res.append(intervals[l])
                l+=1
            elif not newinterval_flag:
                while l<len(intervals) and newInterval[1] >= intervals[l][0]:
                    newInterval = [min(newInterval[0],intervals[l][0]), max(newInterval[1],intervals[l][1])]
                    l+=1
                res.append(newInterval)
                newinterval_flag = True
            else:
                res.append(intervals[l])
                l+=1
        if not newinterval_flag:
            res.append(newInterval)
        return res