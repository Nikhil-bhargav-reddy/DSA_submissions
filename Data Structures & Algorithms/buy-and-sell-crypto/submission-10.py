class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # start with l,r at 0,1 l will be buy date, r will be sell
        # we need max profit, so we kepe checking whereever we have l<r and increment r as l is smaller

        l,r = 0,1

        max_p = 0

        while r<len(prices):
            # print(prices[r], prices[l])


            if prices[l] <=prices[r]:

                max_p = max(prices[r] - prices[l], max_p)
                # now move r because l is at smaller
                r+=1
            else:
                l = r 
                r+=1
        return max_p