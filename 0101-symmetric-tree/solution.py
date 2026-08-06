# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    
        
        def solve(lnode, rnode):
            # base cases
            if lnode is None and rnode is None:
                return True
            if lnode is None or rnode is None:
                return False
            
            # value check
            if lnode.val != rnode.val:
                return False
            
            # recursive mirror check
            return solve(lnode.left, rnode.right) and solve(lnode.right, rnode.left)
        
        return solve(root.left, root.right)