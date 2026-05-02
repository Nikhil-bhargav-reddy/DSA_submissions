# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # simple binary search -> no a bit complex
        # instead of checking if left<root<right etc, we use limits

        # we keep computing limits as we go down the tree

        # again we will use top down approach where we neeed to move form the top to bottom

        # we validate if current value is in limits and go down silently, only if itisnt we return False
        # at the end we return True when none as its valid which will handle it


        def isvalid(root,left,right):
            if not root:
                return True

            if not (left < root.val < right):
                # not valid binary tree
                return False # we return early

            # if valid we delegate to left and rights

            left = isvalid(root.left,left,root.val)
            # when mving left, current roots value will be the max as left should always be smaller than root

            right = isvalid(root.right, root.val, right)
            # when moving right, current value should be minimum of current roots value, right can be infinite for say( obviosuly wont be infinite because at any point theere coule be a left tree above within right main tree)

            return left and right
        return isvalid(root, float('-inf'), float('inf'))
        
                    
