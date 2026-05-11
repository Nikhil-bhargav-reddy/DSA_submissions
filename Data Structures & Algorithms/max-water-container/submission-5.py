class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # logic from math pov is , the bigger the container, the more water
        # we can start from wide containers, l,r at very ends
        # we do r-l = width of container
        # max heright of container could be min of h[l],h[r] because we can only fill till smaller height
        # now comes the pointer movements!! hmm, wait, we can move whicver pinter has amller value? if left has it 
        # we do l+=1, if right has it we do r-=1, all this while we eekp having most = min(l,h)) * widh
        # lets try



# container with most water

# distance between pointers plays a big role
# we do min of pointers values, * len between them

# we move the pointer that is small out of both, all times keeing track of container height using max

        l,r = 0, len(heights)-1
        res = 0

        while l<r:

            h = min(heights[l],heights[r])
            w = r-l

            res = max(res, (h*w))

            if heights[l] <heights[r]:
                l+=1
            else:
                r-=1
        print(res)

            
        return res


