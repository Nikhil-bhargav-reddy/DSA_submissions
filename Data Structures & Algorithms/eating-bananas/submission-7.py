
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 # eating speed of 1
        r = max(piles)
        import math
        min_eat_speed = r
        while l<=r:
            mid = (l+r) //2
            print('checking with eat speed of : ', mid)
            hours = 0
            for i in piles:
                val = math.ceil(i/mid)

                hours+=val

                # if hours >k:
                #     break
            
            if hours > h:
                # we are eating too slow
                # so increment the left to mid
                l = mid+1
            elif hours <=h:
                min_eat_speed = min(min_eat_speed, mid)
                # we are eating well within limits
                # so it will be a good try to check left
                # right could be made as mid
                r = mid - 1
        return min_eat_speed

        # the way this works out is we are doing rounding toward -ve inf
        # so at each stage, if our hours is well under, we simply move right even towards left of mid because mid is already validated
        # so right will be at mid-1 and l keeps incrementing
        # at a stage where l = 4 and r = 5, the mid = 4 works
        # now we try to move r by making r = mid-1 => r will be 4-1 = 3 so r = 3 and l = 4 now thewhile breaks out
        # now we return min we got 