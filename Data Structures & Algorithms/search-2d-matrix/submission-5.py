class Solution:

        # for i in matrix: # check if we are ooking at correct range
        #     if i[-1] == target or i[0] ==target:
        #         return True
        #     elif target < i[-1] and target >i[0]:
        #         # execute binary search, this will be log(n)
        #find_target_in_range logic 
        #         # execute inner binary search
        # return False
# I can probably improvise by adding another binary search for range checks maybe and then trigger inner binary
# outer binary search will see for i [-1] to see if target > i[-1] if yes, we move m to the right and then check if target_range < i[-1]
#check if m's -1 is < target, if yes we also check if m-1's -1 is > target, which means we found the range
    def find_target_in_range(self, i,target):
        l,r = 0, len(i)
        while l<=r:
            m = (l+r)//2
            if i[m] == target:
                return True
            elif target > i[m]:
                l= m+1
            elif target < i[m]:
                r = m-1
        return False

    def find_range(self, matrix, target):
        l,r =0, len(matrix)-1

        while l<=r:
            m= (l+r)//2
            print(m)
            if matrix[m][-1] == target:
                return True
            elif target > matrix[m][-1]:
                l= m+1
            elif target < matrix[m][-1]: 
                print(matrix[m][-1], target)
                # if target less than current max, possibly in range
                # check if target > min of range, if yes we found the range
                if target >= matrix[m][0]:
                    print(matrix[m])
                    return self.find_target_in_range(matrix[m],target)
                # if target is still less than lowest of matrix, we move left to m-1 as the value could be left side
                else:
                    r= m-1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.find_range(matrix,target)

    
