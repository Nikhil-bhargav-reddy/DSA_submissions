class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        # we go deep left first then return coming back with 0, then go right, come back up with 1, 1 for l and r and so on compare max depth at each left and right
        

        return max(left,right) +1 