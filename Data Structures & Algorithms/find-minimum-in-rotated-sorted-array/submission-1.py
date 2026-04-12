class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1

        while l <r:
            mid = (l+r) //2
            print(mid,l,r)
            if nums[mid]>nums[r]: # if mid is greater than right most, means move right
                l = mid+1
            elif nums[mid]<nums[r]:
                r = mid
        return nums[l]          