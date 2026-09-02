# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
 
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        res = [None, 0]

        def helper(root):

            if not root or res[0]:
                return
            
            helper(root.left)

            res[1]+=1

            if res[1] == k:
                res[0] = root.val

            helper(root.right)

        helper(root)

        return res[0]









