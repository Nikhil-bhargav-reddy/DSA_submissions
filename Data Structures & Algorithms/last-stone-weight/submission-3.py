class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-i for i in stones]
        import heapq

        heapq.heapify(stones)

        while len(stones) > 1:

            x = heapq.heappop(stones)

            y = heapq.heappop(stones)

            if x<y:
                y = (y-x)
                heapq.heappush(stones,-y)
            # elif x>y: # not needed because x is guaranteed to be smaller as we pop it first
            #     x = (x-y)
            #     heapq.heappush(stones,-x)

            
        return -stones[-1] if stones else 0