class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0

        l,r=0,0

        lookup = set()

        while r<len(s):
            while s[r] in lookup and l<=r:
                # use conditional loop to slide the left
                lookup.remove(s[l])
                l+=1

            lookup.add(s[r])

            res =  max(res,len(lookup))

            r+=1 # increment r ruthlessly
        return res

                
                



                
