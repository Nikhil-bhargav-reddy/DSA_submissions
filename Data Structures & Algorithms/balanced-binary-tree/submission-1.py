# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        state = [True]

        def helper(root):
            if not root or not state:
                return 0

            left = helper(root.left)
            right = helper(root.right)

            print(left,right)

            if left > right:
                if left - right >1:
                    state[0] = False 
            else:
                if right-left > 1:
                    state[0] = False
            
            return max(left, right) + 1
        helper(root)

        return state[0]
