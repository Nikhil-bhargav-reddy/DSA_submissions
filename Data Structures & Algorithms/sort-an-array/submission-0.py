class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        import heapq


        # using heap sort, we dont need extra space we can heapify input array and return a new res

        heapq.heapify(nums)

        res = []

        while nums:
            val = heapq.heappop(nums)
            res.append(val)
        
        return res