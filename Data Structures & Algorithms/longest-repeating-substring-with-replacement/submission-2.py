class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        hmap={}

        longest = 0

        while l <=r and r<len(s):
            
            if s[r] in hmap:
                hmap[s[r]]+=1
            else:
                hmap[s[r]] = 1

            max_freq = max(hmap.values()) 

            if r-l+1 - max_freq <=k:
                longest = max(longest, r-l+1)                

            else:
                while r-l+1 - max_freq > k:
                    hmap[s[l]]-=1
                    l+=1
            r+=1
            
        print(l,r)
        return longest


            