class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hmap ={}
        n = len(nums)
        for i in nums:
            if i in hmap:
                hmap[i]+=1
            else:
                hmap[i] = 1

            if hmap[i] == (n//2) + 1:
                    return i
        
