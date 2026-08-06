# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr=[]
        def inorder(node):
            if node==None:
                return 
            if node.left:
                inorder(node.left)
            arr.append(node.val)
            if node.right:
                inorder(node.right)   
        inorder(root)
        for i in range(len(arr)):
            if i-1>=0:
              if arr[i-1]>=arr[i]:
                return False
        return True
