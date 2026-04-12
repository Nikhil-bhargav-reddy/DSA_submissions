class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap={}

        for i in range(0,len(nums)):
            reminder= target - nums[i]
        
            if reminder in hmap:
                return [hmap[reminder],i]
            else:
                hmap[nums[i]]=i