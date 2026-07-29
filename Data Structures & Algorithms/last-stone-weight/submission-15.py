import heapq
class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        
        res = []
        if len(stones) == 1:
            return stones[0]
    
        for i in stones:
            heapq.heappush(res,-i)

        
        while len(res) >1:

            x = heapq.heappop(res)
            y = heapq.heappop(res)

            if -x > -y:
                diff = x - (y)

                heapq.heappush(res,diff)

        return -res[0] if res else 0

            