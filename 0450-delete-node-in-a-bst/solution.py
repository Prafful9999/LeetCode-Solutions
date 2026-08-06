# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def solver(node):

            if node is None:
                return None

            if key < node.val:
                node.left = solver(node.left)

            elif key > node.val:
                node.right = solver(node.right)

            else:

                if node.left is None:
                    return node.right

                if node.right is None:
                    return node.left

                temp = node.right
                while temp.left:
                    temp = temp.left

                node.val = temp.val
                node.right = self.deleteNode(node.right, temp.val)

            return node

        return solver(root)
        