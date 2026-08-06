# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def solver(node):
            if node==None:
                return None
            if node.val==val:
                return node
            if val<node.val:
                return solver(node.left)
            if val>node.val:
                return solver(node.right)
        ans=solver(root)
        return ans
            
        