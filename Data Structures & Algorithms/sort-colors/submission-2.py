class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Bubble sort, keep swapping elements, will require o(n) * o(n) operations
        # for i in range(len(nums)):

        #     for j in range(len(nums)):

        #         if j >0 and nums[j] < nums[j-1]:
        #             nums[j],nums[j-1] = nums[j-1],nums[j]
                
        
        # return nums

        # selection sort find lowest value and swap

        i = 0
        min_so_far = [float('inf'),None]

        while i <len(nums):

            for j in range(i,len(nums)):

                if nums[j] < min_so_far[0]: # we found smaller elemnt
                    min_so_far = [nums[j],j]
            print(min_so_far)

            nums[i], nums[min_so_far[1]] = nums[min_so_far[1]], nums[i] # swap smallest with current i

            i+=1

            min_so_far = [float('inf'),None]
        


