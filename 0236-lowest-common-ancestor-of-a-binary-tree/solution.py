# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(self,root,gn):
            stack=[(root,[root])]
            while stack:
                n,path=stack.pop()
                if n==gn:
                    return path
                if n.right:
                    stack.append((n.right,path+[n.right]))
                if n.left:
                    stack.append((n.left,path+[n.left]))
        arr1=dfs(self,root,p)
        arr2=dfs(self,root,q)
        ans=None
        for i in range(min(len(arr1),len(arr2))):
            if arr1[i]!=arr2[i]:
                return ans
            ans=arr1[i]
        return ans
        
                
                




        
        