class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        import heapq

        # stones = [-i for i in stones] can be done but re creates a new space

        for i in range(len(stones)):
            stones[i] = -stones[i]
        # would not take extra space

        heapq.heapify(stones)


        while len(stones) >1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if -(x) >= -(y):
                x = x-y
                heapq.heappush(stones,x)

        return -stones[0] if stones else 0