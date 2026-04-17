class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        l = 0
        n = len(intervals)
        
        # 1. The "Before" phase
        while l < n and intervals[l][1] < newInterval[0]:
            res.append(intervals[l])
            l += 1
            
        # 2. The "During / Overlap" phase ( negation logic!)
        while l < n and not (newInterval[1] < intervals[l][0]):
            newInterval[0] = min(intervals[l][0], newInterval[0])
            newInterval[1] = max(intervals[l][1], newInterval[1])
            l += 1
            
        res.append(newInterval)
        
        # 3. The "After" phase
        while l < n:
            res.append(intervals[l])
            l += 1
            
        return res