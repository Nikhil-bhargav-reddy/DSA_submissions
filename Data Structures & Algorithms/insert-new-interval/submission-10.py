class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l=0
        res=[]
        interval_merged = False

        while l < len(intervals):

            if intervals[l][1] < newInterval[0]: #if current value doesnt have overlap with newinterval
                res.append(intervals[l])
                l+=1
            
            elif not interval_merged:

                while l<len(intervals) and intervals[l][1]> newInterval[0] :
                    newInterval = [min(newInterval[0],intervals[l][0]),max(newInterval[1],intervals[l][1])]
                    l+=1
                
                res.append(newInterval)
                interval_merged = True
            
            else:
                res.append(intervals[l])

        if not interval_merged:
            res.append(newInterval)

        return res