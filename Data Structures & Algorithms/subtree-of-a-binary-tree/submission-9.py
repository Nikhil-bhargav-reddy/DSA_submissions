# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # sub tree of anothe tree 
        # intresting one 
        # we need to keep iterating untill we find the value equal to subrots heads value
        # if equal then we iterate recursion and compare is same tree?
        # if failed, we keep iterating till we find or at None at leaf nodes. 
        state = [False]

        def issametree(p,q):
            if not p and not q:
                return True
            
            if not p or not q:
                return False
            
            if p.val!= q.val:
                return False
            
            return issametree(p.left,q.left) and issametree(p.right,q.right)

        def helper(root):

            if not root or state[0]:
                return None
            
            if root.val == subRoot.val:
                # potential match 
                if issametree(root,subRoot):
                    # if its true we updatee state
                    state[0] = True
                
            helper(root.left)
            helper(root.right)
        
        helper(root)

        return state[0]
        

