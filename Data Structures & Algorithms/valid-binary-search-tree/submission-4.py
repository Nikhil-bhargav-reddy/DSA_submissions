# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(root,lb,rb):

            if not root:
                return True
            
            if not lb < root.val < rb:
                return False
            
            left = helper(root.left,lb,root.val)

            right = helper(root.right, root.val, rb)

            return left and right

        return helper(root,float('-inf'), float('inf'))

        

