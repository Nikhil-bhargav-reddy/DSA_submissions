class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:



        # we need to insert the given new interval in between the intervals or if needed we need to merge if they overlap
        # we use newinterval as anchor to make it clear for us to compare
        # we do -> pre, during, post methods. which is we check pre new interval, not post = during, post interval
        # if newinterval start > intervals[i] end which means no overlap/ pre interval

        # non post = not if new interval end is less than start of ith -> this means its during ( can be reohrased as if new interval start is less than ith end-- idk)
        # post condition is  =  if new interval end is less than start of ith

        res = []

        l = 0

        while l<len(intervals) and newInterval[0] > intervals[l][1]:# no overlap add to res
            res.append(intervals[l])
            l+=1

        while l<len(intervals) and not newInterval[1] < intervals[l][0]: # during condition, which is basically not of post 
            newInterval = [min(newInterval[0], intervals[l][0]), max(newInterval[1], intervals[l][1])]
            l+=1
            

        res.append(newInterval)

        while l<len(intervals):
            res.append(intervals[l])
            l+=1

        return res



