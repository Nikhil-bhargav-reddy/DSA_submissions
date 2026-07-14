# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
 
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        li = []
        def flattener(root, li,k):
            if not root:
                return None

            heapq.heappush(li, -root.val)
            if len(li) > k:
                heapq.heappop(li)


            flattener(root.left, li,k)
            flattener(root.right, li,k)
            
        flattener(root,li,k)

        print(li)

        return -li[0]


