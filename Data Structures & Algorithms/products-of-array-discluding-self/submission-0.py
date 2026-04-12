class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for pos in range(0,len(nums)):
            if not res:
            #if prefix is empty we add 1,  this is because we need a dummy prefix for first element
                res.append(1)
            else:
                prefix_prod = (nums[pos-1]) * (res[-1]) #this logic will get us prefix sum, we check previous pos value and its respective prefix from prefix array so that we dont re compute entire prefixprduct, very inefficient for large arrays
                res.append(prefix_prod)

        product=1
        print(res)
        for i in range(len(nums)-2,-1,-1): #we dont start from the very end because it has postfix of 1 anyway, so we ignore 1 element at the end
            # elements res should be its next elemnts postfix * next element( 4's postfix value * 4 itself)

            product = nums[i+1]*product
            res[i] = res[i]*product

        print(res)
        return res
