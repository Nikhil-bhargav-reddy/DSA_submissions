class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # we should sort first
        # then at each element we iterate we do a two sum 2 in paralell, overall three sum
        # codnitions: we should not stop once we find a two sum pair, we should keep looking
        # our ith element should not be same as next element so we check if i is same as before and skip it as we run i -1 already
        # same for inner two sum, our l cannot be same as prev value
        nums.sort()
        res= []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            else:
                l,r = i+1, len(nums)-1

                while l<r:
                    threeSum = nums[i]+nums[l]+nums[r]

                    if threeSum >0:
                        r-=1
                    elif threeSum <0:
                        l+=1
                    else:
                        res.append([nums[i],nums[l],nums[r]])
                        # we are incrmenting l because we dont want to stop searching for a different pair within two sum
                        # we can do l+=1, but we need to see again if l is not the same as previous if so the res will be same again
                        # lets have a check if l = l+1 then skip
                        # we should do it in while loop as it could be possible that we have multiple vals -2, -2, -2 -2, -1 etc
                        while l<r and nums[l] ==nums[l+1]: # at -2 we see its same, so we keep till l is -2, l+1 is -1, this loop ony takes cre till we reach non dup value
                            l+=1
                        l+=1# this is so that when we end up at
        return res
        