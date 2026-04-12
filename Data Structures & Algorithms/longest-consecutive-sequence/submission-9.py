class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # need to return the length of longest consecutive sequence
        # required space complexity of 0(n)
        # bf approach would be to iteraate over each element to see if any has sequence, back and forth ncube
        # for lookups we can use a hashset -> o(1) time complexity for checking
        lookup = set(nums)

        # check if current element is the start of the sequence by doing if it has -1

        # this way, we avoid checking sequences that could potentially start with lower number
        max_sequence = 0
        for i in lookup:
            if i-1 in lookup: #if lower value exists, we just skip as we can catch it in else clause
                continue
            else: #means this is the start of the sequence
                current_sequence= 0
                start = i
                while start in lookup: # we run this while loop till sequence is valid
                    current_sequence+=1
                    start+=1
                max_sequence = max(max_sequence,current_sequence)
        return max_sequence



                
