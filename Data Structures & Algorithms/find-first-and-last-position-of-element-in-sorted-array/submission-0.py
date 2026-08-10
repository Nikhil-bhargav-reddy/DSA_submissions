class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # our aim is to find the first left occurance of target and last occurance
        # we iterate to find mid first using basic binary search
        # once we find mid, we do not stop, instead store mid == target ina  temp variable
        # and then we will have to find two positions, if we keep moving to right, whats the last target value position we can find
        # if we move left whats the last again
        # overall idea is that, check if target is mid: then move further to find target furthest
        # keep moving left by updatig r = m-1 
        # same for right binary search we update l = m+1

        def left():

            l= 0
            r = len(nums) -1
            temp_res = -1
            while l<=r:
                m =  (l+r)//2

                if target > nums[m]:
                    l = m+1
                
                elif target < nums[m]:
                    r = m-1
                
                else:
                    temp_res = m
                    r = m - 1
            return temp_res

        def right():

            l= 0
            r = len(nums) -1
            temp_res = -1
            while l<=r:
                m =  (l+r)//2

                if target > nums[m]:
                    l = m+1
                
                elif target < nums[m]:
                    r = m-1
                
                else:
                    temp_res = m
                    l = m + 1
            return temp_res
        
        return [left(),right()]


