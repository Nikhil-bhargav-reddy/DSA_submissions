class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l,r = 0,minutes
        res = 0

        intial = 0
        i = 0
        while i < len(customers):

            if i < minutes:
                intial+=customers[i]
            elif grumpy[i] == 0:
                intial+=customers[i]
            
            i+=1

        while r<len(customers):
            res = max(res,intial)
            if grumpy[l] == 1:
                intial-=customers[l]

            if grumpy[r] == 1:
                intial+=customers[r]

            l+=1
            r+=1

            print(intial,res)
        return max(intial,res)





