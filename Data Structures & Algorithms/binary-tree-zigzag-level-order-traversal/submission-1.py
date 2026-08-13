# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # the way we approach this is using normal level order first
        # at each stage or level, we switch to either left to right or right to left
        # stage level can be foudn by using result length
        # if stage len %2 != 0 then we do left right
        # else we do right left

        res = []
        from collections import deque

        q = deque([root])

        while q:
            l = len(q)
            level_tmp = []
            level = len(res)
            for i in range(l):
                node = q.popleft()
                if node:
                    level_tmp.append(node.val)
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
            if level%2 ==0 and level_tmp:
                res.append(level_tmp)
            else:
                if level_tmp: res.append(level_tmp[::-1])
        
        return res


                        


