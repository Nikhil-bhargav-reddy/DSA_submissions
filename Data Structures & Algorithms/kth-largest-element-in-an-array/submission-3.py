class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq



        for i in range(len(nums)): # to keep space to 0(1)
            nums[i] = -nums[i]

        heapq.heapify(nums) # o(1) space and 0(n) time

    
        for i in range(1,len(nums)+1):
            curr =  heapq.heappop(nums) # -( highest)

            if i==k:
                return -curr




