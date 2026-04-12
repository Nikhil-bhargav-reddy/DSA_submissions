class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r= 0, len(nums)-1
        j=0 #see why its failing to debug
        
        while True and j<10:
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
            j+=1 # only to debug remove it after
        return -1


            