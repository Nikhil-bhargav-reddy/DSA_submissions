class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_1 = 0
        l,r = 0,0

        while r<len(nums):

            if nums[r] == 1:
                max_1 = max(max_1, r-l+1)
                r+=1
            else:
                l = r+1
                r = l
        return max_1
            
            