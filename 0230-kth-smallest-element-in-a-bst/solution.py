# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inorder(node,lst):
            if node==None:
                return lst
            if node.left:
                inorder(node.left,lst)
            lst.append(node.val)
            if node.right:
                inorder(node.right,lst)
            return lst
        array=inorder(root,[])
        print(array)
        if array:
          return array[k-1]
        
            
        