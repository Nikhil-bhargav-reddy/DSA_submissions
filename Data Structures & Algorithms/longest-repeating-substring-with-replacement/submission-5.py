class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r =0,0

        hmap = {}

        res = 0

        while r<len(s):
            if s[r] in hmap:
                hmap[s[r]]+=1
            else:
                hmap[s[r]] = 1

            max_freq = max(hmap.values())

            while (r-l+1) - max_freq > k: # 
                hmap[s[l]]-=1
                l+=1
            # calculate the valid subwindow length +k
            res = max(res, r-l+1)
            # seems like we should add first and then check for validation later, got it because we caluculate result after while validation
            r+=1
        return res
            