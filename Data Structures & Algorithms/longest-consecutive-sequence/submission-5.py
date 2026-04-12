class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # need to return the length of longest consecutive sequence
        # required space complexity of 0(n)
        # bf approach would be to iteraate over each element to see if any has sequence, back and forth ncube
        # for lookups we can use a hashset -> o(1) time complexity for checking

        lookup = set(nums)

        res = 0
        # check for the start of the array, if curr-1 exists, its not start of array, else it is

        for i in nums:
            if i-1 in lookup: # min exists, so we start from there
                continue
            else:
                curr = i
                l = 0
                for j in range(len(nums)):
                    if curr in lookup:
                        l+=1
                        curr+=1
                        
                    else:
                        break
                res = max(res,l)
        return res

                
