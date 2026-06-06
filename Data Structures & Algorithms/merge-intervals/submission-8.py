class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        intervals.sort(key=lambda x:x[0])

        for i in intervals:
            if res and res[-1][1] >= i[0]: # if previos intervals end is > current start overlap
                res[-1][1] = max(i[1], res[-1][1])
                # we dont need min between current and prev as we have sorted by starts
            else:
                res.append(i)

        return res