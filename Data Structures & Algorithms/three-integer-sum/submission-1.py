class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # first we need to sort the array
        # now we can do a outer loop to pick first element
        # and do two sum for rest of the elements, using l+r 2sum2
        nums.sort()
        res = []
        for i in range(len(nums)-1):
            if i>0 and nums[i] == nums[i-1]:
                continue
            else:
                print(nums[i+1])
                l,r= i+1,len(nums)-1

                while l<r:
                    threeSum = nums[i]+nums[l]+nums[r]
                    if threeSum >0:
                        r-=1
                    elif threeSum <0:
                        l+=1
                    else:
                        res.append([nums[i],nums[l],nums[r]])
                        l+=1 #because we are not returning, instead we are contining with checking rest of the array for any other matches
                        # we also need to make sure that this l is already iterated over, because it will end up with same result if so
                        # so we move l so that we avoid iterated value of left again, ex: if we have[-2,-2,-2,-2,-1,0,2], we dont want to look at -2 again and again
                        while nums[l] ==nums[l-1] and l<r:
                            l+=1
        return res
        