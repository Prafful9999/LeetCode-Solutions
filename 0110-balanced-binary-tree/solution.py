# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = [True]
        
        def solve(node):
            if node is None:
                return 0
            
            left = solve(node.left)
            right = solve(node.right)
            
            if abs(left - right) > 1:
                flag[0] = False
            
            return 1 + max(left, right)
        
        solve(root)
        return flag[0]