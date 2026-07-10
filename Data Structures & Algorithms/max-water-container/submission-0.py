class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # logic from math pov is , the bigger the container, the more water
        # we can start from wide containers, l,r at very ends
        # we do r-l = width of container
        # max heright of container could be min of h[l],h[r] because we can only fill till smaller height
        # now comes the pointer movements!! hmm, wait, we can move whicver pinter has amller value? if left has it 
        # we do l+=1, if right has it we do r-=1, all this while we eekp having most = min(l,h)) * widh
        # lets try

        l,r = 0, len(height)-1
        most_water =0

        while l<r:
            width = r-l+1
            max_height=min(height[l],height[r])
            curr_water= width * max_height
            most_water = max(curr_water, most_water)
            print(curr_water, width, max_height, height[l], height[r], l ,r)
            if height[l]<=height[r]:
                r-=1
            else:
                l+=1
            
        return most_water
        

