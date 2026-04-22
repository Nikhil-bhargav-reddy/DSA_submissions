class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        max_consec = 0

        for i in nums:
            if i-1 in lookup:
                continue
            else:
                # its the start of the array
                # now we do i+1 checks
                current_max = 0
                while i in lookup:
                    current_max+=1
                    i+=1
                
                # after while breaks, means we are at the end of array
                max_consec =  max(current_max,max_consec)
        return max_consec


                
