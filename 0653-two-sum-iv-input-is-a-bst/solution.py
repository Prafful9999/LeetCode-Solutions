# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        lst=[]
        def inorder(node):
            if node.left:
                inorder(node.left)
            lst.append(node.val)
            if node.right:
                inorder(node.right)
            return lst
        arr=inorder(root)
        print(arr)
        hmap=set()
        for i in arr:
            if k-i in hmap:
                return True
            else:
                hmap.add(i)
        return False


            
        