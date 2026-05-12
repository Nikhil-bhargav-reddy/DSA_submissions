class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:



        # we keep a rolling product basically till the value, not the value

        # product anything before it

        # product anythign after it

        prefix = [1]*len(nums)

        print(prefix)

        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]  # we multiply nums-1 value with its prefix product value basically

        print(prefix)

        postfix = [1]*len(nums)

        for i in range(len(nums)-2,-1,-1):
            postfix[i] = postfix[i+1] * nums[i+1]

        print(postfix)

        return [prefix[i]*postfix[i] for i in range(len(nums))]