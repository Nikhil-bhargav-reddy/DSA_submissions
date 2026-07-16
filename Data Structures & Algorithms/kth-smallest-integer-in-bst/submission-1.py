# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
 
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        state_tracker = [0,None]
        
        def helper(root):
            if not root or state_tracker[1]:
                return None
            
            helper(root.left)
            print(root.val)
            state_tracker[0] = state_tracker[0] + 1

            if state_tracker[0] == k:
                state_tracker[1] = root.val
                return
            helper(root.right)



        helper(root)
        
        return state_tracker[1]


