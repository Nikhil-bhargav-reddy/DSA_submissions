class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r= 0, len(nums)-1
        
        
        while l<=r: # this will fail when l becomes greater than r, due to m+1 and m-1 values
            m = int((l+r)/2)
            print(nums[m],m,l,r)
            if target == nums[m]:
                return m
            elif target >nums[m]:
                # target is towards right of the array
                # so we move left pointer to m's position
                l = m+1
            elif target<nums[m]:
                r = m-1
        return -1


            