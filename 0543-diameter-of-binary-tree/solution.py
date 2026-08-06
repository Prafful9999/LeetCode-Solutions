# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_ht=0
        def solve(node):
            nonlocal max_ht
            if node==None:
                return 0
            left=solve(node.left)
            right=solve(node.right)
            max_ht=max(max_ht,left+right)
            return 1+max(left,right)
        solve(root)
        return max_ht

        