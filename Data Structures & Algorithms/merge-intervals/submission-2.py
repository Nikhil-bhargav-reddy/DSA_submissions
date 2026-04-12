class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key = lambda i:i[0])
        for i in intervals:
            if res and i[0] <=res[-1][1]: # overlapping < =, = because question says even 1,2 2,3 overlap
                    #overlapping
                    prev = res.pop()
                    new_start = min(i[0],prev[0])
                    new_end = max(i[1],prev[1])
                    res.append([new_start, new_end])
            else:
                res.append(i)
        
        return res