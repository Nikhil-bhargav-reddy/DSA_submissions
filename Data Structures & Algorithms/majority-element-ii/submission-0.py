class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        hmap = {}

        for i in nums:
            if i in hmap:
                hmap[i]+=1
            else:
                hmap[i] = 1
            
        res = []

        val = len(nums)/3 # we should probably use ceil? as .5 doesnt mean much considering we want > 2.5 is  >3

        for k,v in hmap.items():
            if v>val:
                res.append(k)
        
        return res

