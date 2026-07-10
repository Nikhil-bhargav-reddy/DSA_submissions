class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hash_set= set()
        l = 0
        longest = 0
        if s==" ":
            return 1
        while l<len(s):
            if s[l] not in hash_set:
                hash_set.add(s[l])
            else:
                print(s[l],l)
                longest = max(longest, len(hash_set))
                hash_set=set() # reset the hash set to empty again
            l+=1
        return max(longest, len(hash_set))


        
           



        
