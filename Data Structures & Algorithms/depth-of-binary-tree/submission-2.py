class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # as soon as we hit the rock bottom or leaf node, we return 0 as it has left as 0 and right as 0

        # now the way this works is with recurison, we are at root, we pause and ask root to give its left and rights
        # we keep doing till the end

        # once we are at the leaf node, 4, we get its left and right as 0's so we do 1+max(left,right)
        # 1+(0,0) = 1
        # now we return this 1 to 3 as left value, right will be 0, so now its 1+(left, right) = 1+(1,0) = 2
        # now we return this to 1, which has 2 which value is 1+(0,0) = 1. now left = 1, right = 2, so we return 1+max(left,right) = 1+max(2,1)
        # we return 3
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1+max(left,right)

        
