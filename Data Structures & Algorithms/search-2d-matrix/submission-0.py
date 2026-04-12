class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        for i in matrix: # check if we are ooking at correct range
            if i[-1] == target or i[0] ==target:
                return True
            elif target < i[-1] and target >i[0]:
                # execute binary search, this will be log(n)
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
                # execute inner binary search
        return False

