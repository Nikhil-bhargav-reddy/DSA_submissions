class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l,r = 0,0
        res = 0
        lookup = set()
        while r<len(s):

            while l<r and s[r] in lookup: # if value is already inside the lookup, duplicate
                lookup.remove(s[r])
                l+=1
            
            lookup.add(s[r])
            res = max(res, r-l+1)

            r+=1
        return res

                
                



                
