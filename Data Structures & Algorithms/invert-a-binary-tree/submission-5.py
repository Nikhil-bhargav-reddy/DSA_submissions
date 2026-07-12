# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # we need to invert the tree, lefts and rights swap basically
        # we can maintain a pointer to hold left value and a pointer to hold right value
        # then assign root.left = right pointer, root.right=left pointer
        # but we should go deep first to find our basecase
        # basecase is if not root: return None
        # we define: if not root: return None then we say left = recursioncall(root.right) , right = recursioncall(root.left) 
        # and now we assign root.left = right , root.right = left and then we return root which will be a inverted tree
        # tracking through logic: where to call recursion here -- intresting, how do we move down first? I think we should call recursion inside the left and right variables
        # trace through now:
        # at 4 as root: we see root.left and root.right and assign to left and right pointers 2, 7 but we should call recursion here because we want to go till None
        # so recursive call for left and recursive call for right means
        # for left, root is 2, root.left is 1, root.right is 3, now they hit another, lets look at 1's recursive call it will return None, same with 3 returns None
        # now 1's recursive calls left and right = None None, so we swap root.left = rights None, and root.right = lefts None
        # now 1's call with return overall root which is 1 as we have return root which is 1, same with 3 will return 3 
        # now back up, to 2's recusive call, it will have left as 1, right as 3, we swap and move up
        # from 2's we get 2 as left and 7 as right, we swap
        # lookig good lets implement 
        if not root: # none basecase at bottom at leafs
            return None
        
        left = self.invertTree(root.left) 
        right = self.invertTree(root.right)

        root.left = right 
        root.right = left 
        # --- WRITE YOUR LOGIC HERE ---
        
        return root