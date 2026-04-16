class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key = lambda i : i[0])

        for i in intervals:
            if res and res[-1][1] >= i[0]: # if last added elements end is > current start we merge

                prev = res.pop()

                new = [prev[0], max(prev[1], i[1])] # we don't need prev[0] and i[0] min because we sorted array anyway

                res.append(new)
            
            else:
                # in case res is empty or if no overlap we add

                res.append(i)

        return res