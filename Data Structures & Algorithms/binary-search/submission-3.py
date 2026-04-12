class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r= 0, len(nums)-1
        j=0 #Hard limit to avoid infinite loop if not found
        
        while j<=len(nums) :
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
            j+=1 # only to limit from infinite looping
        return -1


            