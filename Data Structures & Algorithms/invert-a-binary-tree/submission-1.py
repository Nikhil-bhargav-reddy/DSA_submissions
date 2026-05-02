# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None

        l = self.invertTree(root.left) # l and r will be a simple variable temporarily to store the current left and right so that we can swap
        # but the problem is these variables should be dynamic meaning at leaf nodes left and right, we return none which is fine
        # but at the leaf node itself as root, we want to return root so that our l and r will have actual current root within recursion
        # which is why we will return the root

        # basically at the top, we delegate
        # all the way untill the end when we hit None,None as left and right
        # and we come up by swapping using l,r

        # which is why we will return root, so we dig deep into the end, and start returning root as left and rights
        
        r = self.invertTree(root.right)

        root.left = r
        root.right = l

        return root 