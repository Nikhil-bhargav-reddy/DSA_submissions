# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q: # both are none valid
            return True
        
        if not p or not q: # if only one is None, means false, above condition takes care 
            return False
        
        if p.val != q.val: # when both are not none but not equal
            return False
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right,q.right)

        return left and right # True condition is handled by base cases, they keep propagating up so we good