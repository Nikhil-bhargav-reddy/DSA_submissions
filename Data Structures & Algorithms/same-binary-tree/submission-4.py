# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q: # both null valid same tree
            return True
        
        if not p: # if only one is null
            return False
            
        if not q:
            return False

        if p.val != q.val:
            return False
        
        left = self.isSameTree(p.left,q.left)

        right = self.isSameTree(p.right,q.right)

        return left and right # this will work even though we are not defining any of the True conditions except for null case and this will work
        # overall approach we do is to check if they are not equal and not if they are equal, because thsi will help us return asap as we see a non equal one
        # if we see equal one we kee moving till the end where we have the none case which will yield true all the time, and we would return that finally

        # so, we needed top to bottom approach
        # from top, check each value, if equal move silently, if not equal break out of our recursive loop by providing left, right vals
        
    