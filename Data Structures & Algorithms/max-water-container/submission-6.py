class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]


        # container with most water
        # best way is two pointers starting at both ends
        # do r-l+1  as width and use min(both) as heights and x them
        # now, if rth val is l then we move r-1, else l+=1

        res = 0
        l,r = 0, len(heights)-1

        while l<r: # we could see a huge bar at the middle but it is not a container as its width is 0 so we dont need <=

            width = r-l
            h = min(heights[l], heights[r])

            res = max(res, width*h)

            if heights[l] > heights[r]:
                r-=1
            else: # if l is smaller or equal we move l
                l+=1

        return res


