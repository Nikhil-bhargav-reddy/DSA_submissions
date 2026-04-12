class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l,r =0,0
        max_val = 0
        lookup = set()

        while l<=r and r<len(s):
            while s[r] in lookup:
                # our aim is to make this valid again
                lookup.remove(s[l])
                l+=1
            # not needed else, we can add directly

            lookup.add(s[r])

            max_val = max(len(lookup), max_val)
            r+=1
        return max_val


                
                



                
