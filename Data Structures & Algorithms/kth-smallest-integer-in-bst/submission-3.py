# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
 
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # we want to grab k'th smallest element
        # BST, so we do in order -> left, current , right
        state = [0, None]
        def helper(root):

            if not root or state[0] == k:
                return None
            
            helper(root.left)
            state[0]+=1
            if state[0] == k:
                state[1] = root.val
            helper(root.right)
        
        helper(root)

        return state[1]






