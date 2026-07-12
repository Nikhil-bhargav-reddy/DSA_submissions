class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # we need max depth of this tree, means we need to go deep
# lets say we are at base case or leaf node
# what do we do? return 0 as length and hand it to upper recursive call
# logic: if not root: return 0 base case, left = recursive call on root.left , right = same, return condition will return max(left, right)+1
# this +1 is the current roots length included before handlign back
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right) 

        return max(left, right) +1

        
