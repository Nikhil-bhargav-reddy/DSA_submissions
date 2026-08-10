class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # the idea is, we use two pointers l,r 
        # l holds small values posi
        # r holds large values posi
        # if l<r: we should be fine to do difference and add it to our cumsum
        # if l>r: we move l to r's position, r to l+1
        
        l,r = 0,1
        cum_sum = 0

        while r<len(prices):

            if prices[l] <prices[r]:
                diff = prices[r] - prices[l]
                cum_sum+=diff
                # now that we have added difference, we should move both left and right by one
                l+=1
                r+=1
            else:
                l = r
                r+=1
        
        return cum_sum
