class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pre = [1]*len(nums)
        post = [1]*len(nums)
        # calculate prefix product and postfix products for the value
        # would give us whats the product before and after the value
        # overall multiplying both would give us total product

        for i in range(len(nums)):
            if i >0:
                pre[i] = nums[i-1]*pre[i-1]
            
        for j in range(len(nums)-2,-1,-1):
            post[j] = nums[j+1]*post[j+1]

        for k in range(len(nums)):
            res.append(pre[k]*post[k])

        return res