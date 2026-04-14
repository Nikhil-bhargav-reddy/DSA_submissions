class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)

        l,r = 1, k

        while l<=r:
            mid = int((l+r)/2)
            print('per hour eating rate' , mid)
            curr_hours = 0
            for i in piles:
                hours_to_eat = (i+mid-1)//mid # using a+b-1 //b to round up or can use math.ceil in intvw
                curr_hours+=hours_to_eat
            
            if curr_hours <=h: # valid hourly eating rate, so lets decrease per hour rate by half again
                k = min(k,mid)
                print('valid curr hours', curr_hours, 'current mid is', mid)
                r=mid-1
            elif curr_hours >h: # exceeded hours limit, eating slowly, invalid so should increase or move to other half
                l=mid+1
            print('mid', mid, 'left:', l, 'right', r)

        return k