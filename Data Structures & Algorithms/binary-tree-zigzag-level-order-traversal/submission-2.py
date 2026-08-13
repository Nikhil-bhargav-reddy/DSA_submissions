# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # the way we approach this is using normal level order first
        # if we look closely at expected output, we need to reverse the result of alternatiev levels
        # we can use length of res to see if its even or odd and reverse the levels result accoridngly
        # First implement the standard traversal, then ask whether the required output can be transformed afterward.
        # do not try to revrse the algoritm itself for satifying ouput, do normal level order bfs, then do reverse levels results

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


                        


