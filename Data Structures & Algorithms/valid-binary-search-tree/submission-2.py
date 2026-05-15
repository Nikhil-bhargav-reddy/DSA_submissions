# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # we need to keep using limits, to check if value is within limits to validate and move next
        # we need a function which will let us know if curr value is valid
        def is_valid(root,left,right):
            
            if not root:
                return True
            
            if not (left < root.val <right):
                return False
            
            left = is_valid(root.left,left,root.val) # moving to left means, our max should be roots val
            right = is_valid(root.right,root.val,right)

            return left and right

        return is_valid(root, float('-inf'), float('inf'))

        