# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        q=deque([root])
        res=[]
        flag=True
        while len(q)!=0:
            n=len(q)
            lst=[]
            for i in range(n):
                node=q.popleft()
                lst.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if not flag:
               lst.reverse()
            flag=not flag
            
            res.append(lst)
        return res


        