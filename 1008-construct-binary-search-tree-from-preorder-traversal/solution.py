# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def solver(l,h):
            if l>h:
                return None
            value=preorder[l]
            node=TreeNode(value)
            i=l
            while i<=h and preorder[i]<=value:
                i+=1
            left=solver(l+1,i-1)
            right=solver(i,h)
            node.left=left
            node.right=right
            return node
        return solver(0,len(preorder)-1)

