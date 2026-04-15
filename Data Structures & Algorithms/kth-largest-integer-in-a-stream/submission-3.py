import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.k = k
        self.min_heap = []


        # we can hepafiy our array here, because we are simply going to add values next
        # heapq.heapify(self.nums)

        for i in nums:
            heapq.heappush(self.min_heap, i)
            if len(self.min_heap)>self.k:
                heapq.heappop(self.min_heap)
        # this while loops only keeps the heap's length till it matches the k, this is to only keep top k highest elements
        # heapop will eliminate lowest element, we keep doing it till we acheieve K size only which are highest k ones

    def add(self, val: int) -> int:
        # function to only add the values and return kth largest

        heapq.heappush(self.min_heap, val)

        # now after adding the length becomes k+1, so we pop one small element again
        if len(self.min_heap)>self.k: # this check is mandatory because if input nums is empty, we add one and pop it and return empty again
            heapq.heappop(self.min_heap)

        return self.min_heap[0]



        
