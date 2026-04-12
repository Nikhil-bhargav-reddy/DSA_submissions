class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # need to return the length of longest consecutive sequence
        # required space complexity of 0(n)
        # bf approach would be to iteraate over each element to see if any has sequence, back and forth ncube
        # for lookups we can use a hashset -> o(1) time complexity for checking
        lookup = set()

        for i in nums:
            lookup.add(i)

        # check if current element is the start of the sequence by doing if it has -1

        # this way, we avoid checking sequences that could potentially start with lower number
        max_sequence = 0
        for i in lookup:
            if i-1 in lookup: #if lower value exists, we just skip as we can catch it in else clause
                continue
            else: #means this is the start of the sequence
                current_sequence= 1
                start = i
                for j in range(len(nums)): #wont run forever, breaks if it does not see a sequence
                    if start+1 in lookup:
                        current_sequence+=1
                        start+=1
                    else: # once we no longer find the consecutive elemnt, we break
                        max_sequence = max(max_sequence,current_sequence)
                        break
        return max_sequence



                
