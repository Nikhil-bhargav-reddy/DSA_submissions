import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.k = k
        self.nums = nums


        # we can hepafiy our array here, because we are simply going to add values next
        heapq.heapify(self.nums)

        while len(self.nums) > k:
            heapq.heappop(self.nums)
        # this while loops only keeps the heap's length till it matches the k, this is to only keep top k highest elements
        # heapop will eliminate lowest element, we keep doing it till we acheieve K size only which are highest k ones

    def add(self, val: int) -> int:
        # function to only add the values and return kth largest

        heapq.heappush(self.nums, val)

        # now after adding the length becomes k+1, so we pop one small element again
        if len(self.nums)>self.k: # this check is mandatory because if input nums is empty, we add one and pop it and return empty again
            heapq.heappop(self.nums)

        return self.nums[0]



        
