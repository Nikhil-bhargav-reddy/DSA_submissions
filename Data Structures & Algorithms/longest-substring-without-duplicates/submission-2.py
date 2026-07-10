class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hash_set= set()
        l = 0
        longest = 0
        
        while l<len(s):
            if s[l] not in hash_set:
                hash_set.add(s[l])
                l+=1
            else:
                print(hash_set)
                longest = max(longest, len(hash_set))
                hash_set=set() # reset the hash set to empty again

        return longest


        
           



        
