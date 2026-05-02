class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root: # base case where we are at the leaf node, we dont have a depth for left or right, so will be 0
            return 0
        
        left = self.maxDepth(root.left)

        right = self.maxDepth(root.right) # will iterate to 0 at the base case and our return will give 1 +0,0 so we will keep on incrmeenting 1 up while selecting max of both right and left
        
        return 1 + max(left,right) # considering base case, the left and right values will be 0, so we come up with current root's depth and max of leaf nodes depth

        
