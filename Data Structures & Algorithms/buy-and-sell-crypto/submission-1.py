class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy on lower day, sell on higher to make max
        # if today > tomorrow, we skip buying today
        # l,r keep moving these by checking max profit
        max_profit = 0

        l,r = 0,1

        while l<r and r<len(prices):
            if prices[l] <prices[r]: #we make some profit
                max_profit = max(max_profit,prices[r]-prices[l])
                r+=1
            else: #move both pointers
                l= r
                r+=1
        return max_profit