# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # we swap elements of left to right from the bottom

        if not root:
            return None
        
    
        
        left = self.invertTree(root.left)

        right = self.invertTree(root.right)

        root.left = right

        root.right = left

        return root

        # all we are doing is captureing left node in a left stiky note
        # right in a right sticky note
        # and swapping both the sticky notes on root, so now they both are to opposite sides
        # left, right basically holds the nodes address from there below