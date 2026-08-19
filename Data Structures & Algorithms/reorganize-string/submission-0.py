class Solution:
    def reorganizeString(self, s: str) -> str:
        # max heap to store all the values
        # temp variable 
        # we store the first popped in temp variable by reducing its frewuency by 1
        # add that value (a) to res
        # now when we have popped next element from heap
        # added it to res 
        # add back the gemp to heap
        # assign temp variable to the recently popped
        # return if the root of heap is > half the length of array as ''

        import heapq
        hmap = {} # i know we can use counters direcyly but i pefer to code it
        for i in s:
            if i in hmap:
                hmap[i]+=1
            else:
                hmap[i] = 1
        print(hmap)

        max_heap= []

        for k,v in hmap.items():
            heapq.heappush(max_heap, [-v,k])

        print(max_heap)

        temp = None
        res = ''
        while max_heap:
            val= heapq.heappop(max_heap)
            print(val, max_heap)
            res+=val[1]
            if temp:
                heapq.heappush(max_heap, temp)
            if val[0]+1 < 0:
                temp = [val[0]+1, val[1]]
            else:
                temp = None
        
        return res if len(res) == len(s) else ''

            


