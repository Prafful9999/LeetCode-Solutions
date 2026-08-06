# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node=root
        node2=root
        lst1=[]
        lst2=[]
        if root==None:
            return None
        while p.val!=node.val:
            lst1.append((node.val,node))
            if node.val>p.val:
                node=node.left
            else:
                node=node.right
        while q.val!=node2.val:
            lst2.append((node2.val,node2))
            if node2.val>q.val:
                node2=node2.left
            else:
                node2=node2.right
        
        lst1.append((node.val,node))
        lst2.append((node2.val,node2))
        ans=root
        i=0
        while i<min(len(lst1),len(lst2)):
            if lst1[i]==lst2[i]:
                ans=lst1[i][1]
            else:
                break
            i=i+1
        return ans
        
        
        
        
        
        
                
        

        