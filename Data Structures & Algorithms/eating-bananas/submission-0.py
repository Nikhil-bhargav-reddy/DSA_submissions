class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        min_eating_speed = 1 # we can start with 1 banana per hour
        max_eating_speed= max(piles) # maximum could be 1 pile at a time
        res = max_eating_speed
        while min_eating_speed <= max_eating_speed:
            hour_tracker=0
            avg_speed = int(((max_eating_speed+min_eating_speed) / 2))

            for i in piles:
                print(i)
                hour_tracker +=(math.ceil(i/avg_speed))
            
            print(hour_tracker,avg_speed)
            if hour_tracker <= h:
                # we found ideal eating speed
                res= min(res,avg_speed)
                max_eating_speed = avg_speed-1
            elif hour_tracker >h:
                # we ate slowly, more hours = eating speed is slow
                # make avg_speed+1 as min now
                min_eating_speed = avg_speed+1

        return res