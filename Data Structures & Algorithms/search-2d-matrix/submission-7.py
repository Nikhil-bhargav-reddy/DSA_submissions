class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1

        while l<=r:
            mid = (l+r) //2

            if target > matrix[mid][-1]:
                # move right, increment l
                l = mid+1
            
            elif target < matrix[mid][0]:
                # before so move r to left
                r = mid-1
            else:
                # potentially here
                inner_l = 0
                inner_r = len(matrix[mid])-1

                while inner_l <= inner_r:
                    inner_mid  =  (inner_l +inner_r) //2
                    if target == matrix[mid][inner_mid]:
                        return True
                    elif target > matrix[mid][inner_mid]:
                        # towards right
                        inner_l =  inner_mid+1
                    elif target < matrix[mid][inner_mid]:
                        inner_r =  inner_mid -1
                return False
        return False