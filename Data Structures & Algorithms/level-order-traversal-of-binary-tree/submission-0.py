# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # queue to keep track of current element 
        # queues hold nodes actual nodes, not values of nodes
        # we initialize queue with root
        # while q -> create a level list
        # within q: we pop left as x
        # levellist.append(x)
        # x.left append to queue, x.right appendto queue
        # repeat untill q is empty = no nodes left
        # can throw in a bunch of if's to avoid none or null nodes
        res = []
        
        q = deque()

        q.append(root)

        while q:
            level = []
            leng = len(q)

            for i in range(leng):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level: res.append(level)
        
        return res




