# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p==None and q==None:
            return True
        elif p!=None and q==None:
            return False
        elif p==None and q!=None:
            return False
        else:
            flag=[True]
            def solve(p,q):
                if (p.left==None and p.right==None) and (q.right==None and q.left==None):
                    if p.val!=q.val:
                        flag[0]=False
                        return flag
                    return flag
                if p.val!=q.val:
                    flag[0]=False
                    return flag
                if (p.left and p.right) and (q.left and q.right):
                    solve(p.left,q.left)
                    solve(p.right,q.right)
                elif (p.left!=None and p.right==None) and (q.left!=None and q.right==None):
                    solve(p.left,q.left)
                elif (p.left==None and p.right!=None) and (q.left==None and q.right!=None):
                    solve(p.right,q.right)
                else:
                    flag[0]=False
                    return flag

            solve(p,q)
            
            return flag[0]
            