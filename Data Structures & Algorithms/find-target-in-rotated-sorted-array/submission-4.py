class Solution:
    def find_min(self, nums):
        l,r = 0, len(nums)-1
        while l<r:
            m = (l+r)//2
            # do a minimum search first , then find the pivot value, now basically do a normal binary search 
            # find minimum first

            if nums[m] > nums[r]:
                # check right
                l = m+1
            elif nums[m] < nums[r]:
                r = m 
        print(r)    
        return r

    def binary_search(self, nums, target,l,r):
        while l<=r:
            print(nums[l], nums[r], l, r)
            mid = (l+r)//2
            if nums[mid] == target:
                return mid 
            elif nums[mid] > target:
                r = mid-1         
            elif nums[mid] < target:
                l = mid+1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        pivot_loc = self.find_min(nums)

        if nums[pivot_loc] <= target <= nums[r]:
            return self.binary_search(nums,target, pivot_loc, r)
        else:
            return self.binary_search(nums,target, l, pivot_loc-1)
            

        

