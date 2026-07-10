class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        hmap={}

        longest = 0

        while l <=r and r<len(s):
            print(hmap)
            
            max_freq = max(hmap.values()) if hmap else 0
            while not r-l+1 - max_freq <=k:
                hmap[s[l]]-=1
                l+=1
            
            
            if r in hmap:
                hmap[s[r]]+=1
            else:
                hmap[s[r]] = 1
            r+=1
            longest = max(longest, r-l+1)
        return longest


            