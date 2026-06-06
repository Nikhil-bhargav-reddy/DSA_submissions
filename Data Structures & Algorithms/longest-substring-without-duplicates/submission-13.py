class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        lookup = set()

        l,r = 0,0

        res = 0

        while r<len(s):

            while lookup and s[r] in lookup: # as long as the r value is in lookup, we iterate this till its gone duplicate
                lookup.remove(s[l])
                l+=1

            lookup.add(s[r])

            res = max(res, len(lookup)) # by here lookup is already clean from dups

            r+=1 # move regardless

        return res


                
                



                
