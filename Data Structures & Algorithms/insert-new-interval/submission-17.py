class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # three way approach
        # before new interval - simply add to res
        # after new interval - simply add to res
        # if both not - then its during - merge and add

        l = 0
        res = []
        while l< len(intervals) and intervals[l][1] < newInterval[0]:
            res.append(intervals[l])
            l+=1
        
        while l< len(intervals) and not intervals[l][0] > newInterval[1]:
            # we are checking not after condition = during , easy for intution
            newInterval = [
                min(intervals[l][0], newInterval[0]),
                max(intervals[l][1], newInterval[1])
            ]
            l+=1
        res.append(newInterval)
        
        while l< len(intervals) and intervals[l][0] > newInterval[1]:
            res.append(intervals[l])
            l+=1

        return res
