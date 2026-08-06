# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def left_ht(n):
            h=0
            while n:
                h+=1
                n=n.left
            return h
        def right_ht(n):
            h=0
            while n:
                h+=1
                n=n.right
            return h

        def solve(node):
            if root==None:
              return 0
            lh=left_ht(node)
            rh=right_ht(node)
            if lh==rh:
                return 2**lh-1
            return 1+solve(node.left)+solve(node.right)
        ans=solve(root)
        return ans        
        

        