class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        for i in range(len(stones)):

            stones[i] = -stones[i]

    

        heapq.heapify(stones)

    
        while len(stones)> 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)

            print(x,y)
            if x==y:
                continue
            elif x>y:
                x = x-y
                heapq.heappush(stones,-x)
            # we could add else where y>x but relaistically this isnt possible as we are popping from max heap so x will always be greater or equal to y

        return -stones[0] if stones else 0