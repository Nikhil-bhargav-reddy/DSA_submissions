class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l=0
        newinterval_flag = False
        res= []
        while l<len(intervals):
            if intervals[l][1] < newInterval[0]:
                res.append(intervals[l])
                l+=1
            elif not newinterval_flag:
                newInterval = [min(newInterval[0],intervals[l][0]), max(newInterval[1],intervals[l][1])]
                res.append(newInterval)
                l+=1

                if l<len(intervals) and res[-1][1] >= intervals[l][0]:
                    prev = res.pop()
                    new = [min(prev[0],intervals[l][0]), max(prev[1], intervals[l][1])]
                    res.append(new)
                    l+=1
                    newinterval_flag = True
            else:
                res.append(intervals[l])
                l+=1

        return res