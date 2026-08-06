# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def solver(node):
            if node==None:
                return None
            if node.val==p.val:
                return node
            if node.val==q.val:
                return node
            left=solver(node.left)
            right=solver(node.right)
            if left!=None and right!=None:
                return node
            elif (left==None and right!=None) or (left!=None and right==None):
                if left!=None:
                    return left
                if right!=None:
                    return right
            else:
                return None
        return solver(root)
            
        