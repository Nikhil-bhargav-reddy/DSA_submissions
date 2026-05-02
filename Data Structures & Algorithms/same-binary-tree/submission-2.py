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

        return True if left and right else False
    