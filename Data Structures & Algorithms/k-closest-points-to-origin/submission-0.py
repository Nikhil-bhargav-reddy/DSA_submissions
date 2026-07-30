import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def distance(a):
            res = (a[0]**2) + (a[1]**2)

            print(res)
            return res

        heap_t = []

        for i in range(len(points)):
            # max heap implementation as we want to pop out maxes
            dist =  distance(points[i])
            print(dist)
            heapq.heappush(heap_t, (-dist,i))
            # we push in tuples of distance and i, heap will be sorted by distance anyway as its first element

            if len(heap_t) > k:
                heapq.heappop(heap_t) # keeps eliminating largest
        
        final_res = []
        for i in heap_t:
            final_res.append(points[i[1]])
        
        return final_res

            
        

        
