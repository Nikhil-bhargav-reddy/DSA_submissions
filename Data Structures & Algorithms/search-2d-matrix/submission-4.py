class Solution:

    def binary_search(self,li,target):
        print('running binary search logic')
        left,right = 0, len(li)-1
        while left<=right :
            m = (left+right) //2
            
            if li[m] == target:
                return True
            elif li[m] >target:
                right= m-1
            else:
                left = m+1
            
        print('target isnt found')

        return False


    def searchMatrix(self, matrix, target):
        l, r = 0, len(matrix)-1

        while l<=r:

            mid = (l+r)//2
            print('mid value being looked up', matrix[mid],mid,l,r)
            if matrix[mid][-1] > target: # if mid's end is > target, means target is to left
                if matrix[mid][0]<target:
                    # found the array we need
                    # do the binary here
                    print('Binary search array is here', matrix[mid])
                    return self.binary_search(matrix[mid],target)
                elif matrix[mid][0] > target:
                    # move left here because value isnt in the mid array
                    r =  mid-1
                else:
                    print('well we found the guy', matrix[mid][0])
                    return True
            
            elif matrix[mid][-1] < target:# target could be to the right
                print(matrix[mid][-1], target)
                l = mid+1
            else:
                return True
        return False

    
