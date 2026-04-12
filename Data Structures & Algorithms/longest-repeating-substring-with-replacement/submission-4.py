class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r =0,0
        hmap={}
        longest = 0
        while l<=r and r<=len(s)-1:
            
            if s[r] in hmap:
                hmap[s[r]]+=1
            else:
                hmap[s[r]] =1

            most_freq = max(hmap.values())
            
            while (r-l+1) - most_freq>k and l<r:
                if s[l] in hmap:
                    hmap[s[l]]-=1
                l+=1 # incrment L till substring is valid

            longest = max(longest, r-l+1)

            r+=1
        return longest
            