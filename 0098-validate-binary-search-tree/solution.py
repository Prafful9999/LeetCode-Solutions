# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def solver(node, l, h):
            if node == None:
                return True

            if not (l < node.val < h):
                return False

            if not solver(node.left, l, node.val):
                return False

            if not solver(node.right, node.val, h):
                return False

            return True

        return solver(root, float('-inf'), float('inf'))