class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # We need a separate variable to store the absolute highest number we've seen
        self.highest_depth_seen = 0
        
        # We create a helper function that takes the node AND its current level
        def dfs(node, current_level):
            if not node:
                return
            
            # 1. Update our global record if this level is the deepest we've gone
            self.highest_depth_seen = max(self.highest_depth_seen, current_level)
            
            # 2. Tell the children to go 1 level deeper
            dfs(node.left, current_level + 1)
            dfs(node.right, current_level + 1)
            
        # Kick off the recursion starting at level 1
        dfs(root, 1)
        
        return self.highest_depth_seen