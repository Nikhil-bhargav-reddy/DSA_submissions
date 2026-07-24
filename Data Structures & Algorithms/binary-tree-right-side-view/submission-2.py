# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()

        res = []

        q.append(root)

        while q:
            level = len(q)
            for i in range(level):
                node = q.popleft()
                if node and node.left: q.append(node.left)
                if node and node.right: q.append(node.right)
                
            if node: 
                res.append(node.val)
        
        return res