# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root_ind=0
        def solver(low,high):
            nonlocal root_ind
            if low>high:
                return None
            i=0
            while inorder[i]!=preorder[root_ind]:
                i+=1
            root_ind+=1
            root_val=inorder[i]
            root=TreeNode(root_val)
            root.left=solver(low,i-1)
            root.right=solver(i+1,high)
            return root
        return solver(0,len(inorder)-1)
            
            
        


        