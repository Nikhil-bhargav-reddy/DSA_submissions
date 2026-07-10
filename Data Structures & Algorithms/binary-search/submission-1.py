class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r= 0, len(nums)-1
        j=0 #see why its failing to debug
        
        while True and j<10:
            m = (l+r)//2
            print(nums[m])
            if target == nums[m]:
                return m
            elif target >nums[m]:
                # target is towards right of the array
                # so we move left pointer to m's position
                l = m
            elif target<nums[m]:
                r = m
            j+=1 # only to debug remove it after
        return -1


            