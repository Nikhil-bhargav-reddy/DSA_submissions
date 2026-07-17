# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def issame(p,q):
            if not p and not q: # if both are null complelety valid
                return True
            
            if not p or not q:
                # print('either of of them arent valid', p.val, q)
                return False
                # if just p is not none or just q
            
            if p.val!=q.val:
                # print('both arent equal p:',p, 'q: ',q)
                return False # we fail fast if its not equal

            # print('executing left:', p.left, q.left)

            left = issame(p.left,q.left)
            
            right = issame(p.right,q.right)

            # print('l and r are',left and right)
            
            return left and right # if both are True then only true

        if not root:
            return False

        # print('main loop beginning with', root.val, subRoot.val)

        
        if issame(root,subRoot):
            return True
                # can combine this with below to simply, anyway we have spend enough time for trying this
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot) # we need only one confirmation that the result is correct

        # I think i understand the issue, we are not storing the state of the recursive checks
        # for example in cases where we end root with subroot: ex 12345 245 we will be fine because we return whatever is output of issame tree
        # wait how are we handling cases where root.val equals subroot.val but false, then we check further if another node potentially matches?
        # we should not return directly, we should store the answer somwehere 
        # no the return in middle is handling it, if we fail on left tree, right tree will handle it, so either one captures it
        # we are fine correctly logging, its just that we dont need state, my bad i was over complicating - or can do with state too
        # as long as state isnt true and root isnt none, we coule iterate. hmm nvm
        # the issue is when we have same nodes ex: 1,1 vs 1 then only our last fun runs and says False, we should loop further
        # I mean we should call issubtree functions even during both root vals are equal if the return value is False