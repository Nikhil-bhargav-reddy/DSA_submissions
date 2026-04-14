class Solution:
# if target exists in the given matrix?

# we start at mid by l+r//2 r is len

# at mid we check if mid's end value is > target

# if yes, target is towards left, so we make r = mid-1 need to be careful here because the value coudl be in right one itself


# if mids end < target, target is towards right, so we make l = mid+1 , same careful
#l,r = 0,4
#mid = 2
# mid[-1] == 17 which is < 40
# so we make l= mid+1 = 3

# mid = 3+4 //2 = 3
# if mid[-1]w which is 43 > 40 means to the left we have hope
# check if mid[0] <40, so now this is the final binary search lookup
    #lef, rig = 0, len(mid)
    #simple binrary search to lookup
# if mid[0] > 40, now we move left so r = mid-1
# it goes on
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
    
