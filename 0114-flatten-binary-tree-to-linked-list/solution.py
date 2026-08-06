# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        '''
        Do not return anything, modify root in-place instead'''
        

        curr = TreeNode(0)
        head = curr

        def solver(node):
            nonlocal curr

            if node is None:
                return

            left = node.left
            right = node.right

            curr.right = node
            curr.left = None
            curr = curr.right

            solver(left)
            solver(right)

        solver(root)

        root = head.right


        