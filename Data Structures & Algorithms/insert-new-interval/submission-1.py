class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        l =0
        newint = False

        while l <len(intervals):
            
            
            newInterval_start = newInterval[0]
            newInterval_end = newInterval[1]

            if res:
                if res[-1][1] >= intervals[l][0]:
                    print(res[-1][1], intervals[l][0])
                    prev = res.pop()

                    new = [min(prev[0], intervals[l][0]), max(prev[1], intervals[l][1])]

                    res.append(new)
                    l+=1

                elif res[-1][1] >= newInterval[0] and not newint: # new interval comes here to merge
                    
                    prev = res.pop()

                    new = [min(prev[0], newInterval[0]), max(prev[1], newInterval[1])]

                    res.append(new)
                    newint = True
                
                else:
                    if newInterval[0] < intervals[l][0] and not newint: # to handle first element is new interval case
                        print('l')
                        res.append(newInterval)
                        newint = True
                    else:
                        res.append(intervals[l])
                        l+=1
            else:
                if newInterval[0] < intervals[l][0] and not newint: # to handle first element is new interval case
                    res.append(newInterval)
                else:
                    res.append(intervals[l])
                l+=1

        return res