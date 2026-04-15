class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        nums_h = [] # empty list is a heap in python

        for i in nums:
            heapq.heappush(nums_h, i)
            if len(nums_h) >k:
                heapq.heappop(nums_h) # with this we strictly maintain the size of the heap to k to have top k
        return nums_h[0]


