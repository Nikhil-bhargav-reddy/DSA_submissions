class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq



        res = []

        for i in nums:
            if len(res) > k:
                heapq.heappop(res)
            else:
                heapq.heappush(res,i)
        return res[0]

