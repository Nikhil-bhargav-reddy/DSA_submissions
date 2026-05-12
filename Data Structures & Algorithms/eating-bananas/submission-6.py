class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        l,r = 1, max(piles)
        res = r
        while l<=r:
            mid = (l+r)//2
            print('eating speed' ,mid)
            curr_hrs = 0

            for i in piles:
                curr_hrs+= math.ceil(i/mid)

            if curr_hrs <= h: # ate faster than required, so we add to result and make mid as our max so we can look for smaller speed
                res = min(res,mid)
                r = mid - 1
            elif curr_hrs > h: # we ate slower than required
                l = mid+1

        return res