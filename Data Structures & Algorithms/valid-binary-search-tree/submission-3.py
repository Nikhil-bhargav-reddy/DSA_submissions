# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # valid bst
        # use boundaries
        # begin with - inf and + inf
        # when moving left, right boundary becomes root
        # when moving right, left bounday becomes root
        # keep moving, should use top down processing

        def isValid(root, left_b, right_b):

            if not root:
                return True
            
            if not left_b < root.val < right_b:
                return False
            
            left = isValid(root.left, left_b, root.val)
            right = isValid(root.right, root.val, right_b)

            return left and right
        
        return isValid(root, float('-inf'), float('inf'))