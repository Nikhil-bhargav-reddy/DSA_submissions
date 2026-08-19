class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        import heapq
        from collections import deque

        hmap = {}

        for i in tasks:
            if i in hmap:
                hmap[i]+=1
            else:
                hmap[i] = 1
        
        # print(hmap)
        max_heap = []
        for k,v in hmap.items():
            heapq.heappush(max_heap,[-v,k])
        
        # print(max_heap)

        timer = 0 
        q = deque([])
        while max_heap or q:
            # print(timer)
            if max_heap:
                val = heapq.heappop(max_heap)

                # removed one value , processed one basically
                val[0] = val[0]+1

                if val[0] < 0:# should not be 0 or > consier we use -
                    value = (val[0], val[1], timer) # we get the timer at that iteration when it was added
                    q.append(value)
                
            if q and timer - q[0][-1] >= n: # if the first value in queue has crossed the time, we are ready to pop and add it back to our hea
                    
                node = q.popleft()
                heapq.heappush(max_heap, [node[0], node[1]])
                
            timer+=1 

        return timer






