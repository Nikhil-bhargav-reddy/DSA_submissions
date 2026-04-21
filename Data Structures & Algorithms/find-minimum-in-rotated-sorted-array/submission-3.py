class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1

        while l<r:
            mid = (l+r)//2
            print(l,r,mid)
            if nums[mid] > nums[r]: # min is towards right
                l = mid+1
            elif nums[mid] < nums[r]:
                r = mid
        return nums[l]