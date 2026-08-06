# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        head=root
        if root is None:
            return TreeNode(val)
        def solver(node):
            if val<node.val:
                if node.left:
                    solver(node.left)
                else:
                    node.left=TreeNode(val)
                    return
            else:
                if node.right:
                    solver(node.right)
                else:
                    node.right=TreeNode(val)
                    return
        solver(root)
        return head
        
                
            
            