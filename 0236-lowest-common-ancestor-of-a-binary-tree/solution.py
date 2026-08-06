# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def solve(self,node,p,q):
            if node==None:
                return None
            if node==p or node==q:
                return node
            left=solve(self,node.left,p,q)
            right=solve(self,node.right,p,q)
            if left is None and right is None:
                return None
            elif left is None:
                return right
            elif right is None:
                return left
            return node
        return solve(self,root,p,q)

            
        