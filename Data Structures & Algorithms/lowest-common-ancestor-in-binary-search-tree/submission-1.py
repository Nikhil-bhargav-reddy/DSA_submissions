# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # intution:
        # the requirement is that we return the place where these numbers have split off
        # at which point the numbers are seperated, example 3,5 seperated at 4, 
        # 0,4 seperated at 2
        # fine, lets ignore the itself case for the moment, we will handle at the end
        # advantage of binary SEARCH tree is that we can bisect into halfs and dont need to search unwanted parts so logn
        # now its how? so our input function already takes root, p,q
        # so we can have a simple top down approach
        # we check if p.val < root.val < q.val: return root
        # we can propagate this to left and rights
        # wait, its binary search, so I think we can either call left or right based on we go down
        # if q.val < root.val: left execute
        # else right execute
        # lets code
        if not root:
            return None
        if q.val>p.val:
            if p.val <= root.val <= q.val: 
                # will return directly the root at first condition itself if true else we progapate
                # we can have this as = because we want t satify decsendant of itself
                return root
            if q.val < root.val: # means both p and q are to left so we only execute left recursion
                return self.lowestCommonAncestor(root.left, p, q)
            else:
                return self.lowestCommonAncestor(root.right, p, q)
        else:
            if q.val <= root.val <= p.val: 
                # will return directly the root at first condition itself if true else we progapate
                # we can have this as = because we want t satify decsendant of itself
                return root
            if p.val < root.val: # means both p and q are to left so we only execute left recursion
                return self.lowestCommonAncestor(root.left, p, q)
            else:
                return self.lowestCommonAncestor(root.right, p, q)