class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        tmp_res = [-1]*len(nums2)
        stk = []
        for i in range(len(nums2)):

            while stk and nums2[i] >stk[-1][0]:
                num,idx = stk.pop()
                tmp_res[idx] = nums2[i] # next greater for that index
            
            stk.append((nums2[i],i))
        
        print(tmp_res, stk)
        hmap ={}

        for i in range(len(nums2)):
            if not nums2[i] in hmap:
                hmap[nums2[i]] = tmp_res[i]
        
        print(hmap)
        res =[]
        for i in nums1:
            res.append(hmap[i])
        
        return res



